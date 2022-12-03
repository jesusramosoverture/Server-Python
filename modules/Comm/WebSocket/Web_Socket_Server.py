#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" TODO: WEBSOCKET SERVER"""
# ---------------------------------------------------------------------------
import logging
import traceback
from dataclasses import dataclass, field
from threading import Lock
# ---------------------------------------------------------------------------
from PyQt5 import QtWebSockets, QtNetwork
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
# ---------------------------------------------------------------------------
from modules.Comm.WebSocket.MessageProcessor import MsgProcessor
from modules.Utils.SystemStatus import SystemStatus

# Setting logging module
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]

@dataclass
class QtServer(QObject):
    """
    """

    ipaddress: str
    port: int
    parent: QtWebSockets.QWebSocketServer
    rcvdMsg = pyqtSignal(str)
    connection = pyqtSignal(bool)
    on_close_connection_signal = pyqtSignal()

    def __post_init__(self):
        """

        :return:
        """
        super(QtServer, self).__init__()
        __metaclass__ = SingletonMeta

        print(f"self.ipaddress: {self.ipaddress}")
        self.clients = []
        self.processor = MsgProcessor()
        self.server = QtWebSockets.QWebSocketServer(self.parent.serverName(), self.parent.NonSecureMode, self.parent)
        self.set_up_listener()
        self.set_up_max_pending_connections(False)
        self.server.newConnection.connect(self.on_new_connection)
        self.system_status = SystemStatus()

    def localhost_or_ipaddress(self):
        """

        :return:
        """
        return self.ipaddress == "localhost"

    def set_up_listener(self):
        """

        :return:
        """
        if self.localhost_or_ipaddress():
            self.listen = self.server.listen(QtNetwork.QHostAddress(QtNetwork.QHostAddress.LocalHost), self.port)
        else:
            self.listen = self.server.listen(QtNetwork.QHostAddress(self.ipaddress), self.port)

    def on_new_connection(self):
        """

        :return:
        """
        try:
            self.set_up_client()
            self.clients.append(self.client_connection)
            self.set_up_max_pending_connections(True)
        except OSError:
            log.error(traceback.format_exc())

    def set_up_client(self):
        """

        :return:
        """
        try:
            self.client_connection = self.server.nextPendingConnection()
            self.client_connection.textMessageReceived.connect(self.processTextMessage)
            self.client_connection.binaryMessageReceived.connect(self.processBinaryMessage)
            self.client_connection.disconnected.connect(self.socket_disconnected)
            self.client_connection.sendTextMessage("hola. Estoy aqui")
            self.system_status.new_client_connected = True
            self.list_of_audio_devices()
        except OSError:
            log.error(traceback.format_exc())

    def processTextMessage(self, message):
        """

        :param message:
        :return:
        """
        if self.client_connection:
            logging.info(message)
            self.processor.process_the_message(message)
            self.rcvdMsg.emit(message)
            self.client_connection.sendTextMessage(message)

    def processBinaryMessage(self, message):
        """

        :param message:
        :return:
        """
        if self.client_connection:
            self.client_connection.sendBinaryMessage(message)

    def socket_disconnected(self):
        """

        :return:
        """
        try:
            if self.client_connection:
                self.clients.clear()
                self.client_connection.close()
                self.set_up_max_pending_connections(False)
                self.client_connection.deleteLater()
                self.on_close_connection_signal.emit()
        except OSError:
            log.error(traceback.format_exc())

    def set_up_max_pending_connections(self, is_connection):
        """

        :param is_connection:
        :return:
        """
        if is_connection:
            self.server.setMaxPendingConnections(0)
        else:
            self.server.setMaxPendingConnections(1)

    @pyqtSlot()
    def disconnect_client_from_server(self):
        try:
            self.socket_disconnected()
        except OSError:
            log.error(f"Error when disconnect_client_from_server: {traceback.format_exc()}")

    @pyqtSlot()
    def list_of_audio_devices(self):
        if self.client_connection:
            speakers_list = tuple(self.system_status.get_all_speakers)
            for speaker in speakers_list:
                print(speaker)
            audio_device_msg = {"Id": 200, "order":
                {"speakers": {speakers_list}
                    , "current_speaker": {self.system_status.active_speaker}
                 }}
            log.info(audio_device_msg)
            self.client_connection.sendTextMessage(str(audio_device_msg))

    def send_a_msg(self, msg ) -> None:
        """

        :param msg_to_send:
        :return:
        """
        self.client_connection.sendTextMessage(msg)
