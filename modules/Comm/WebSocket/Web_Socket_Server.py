import typing

from PyQt5 import QtWebSockets, QtNetwork
from PyQt5.QtCore import QObject, pyqtSignal
from dataclasses import dataclass
import logging
import traceback

from PyQt5.QtWebSockets import QWebSocket

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@dataclass
class QtServer(QObject):
    ipaddress: str
    port: int
    parent: QtWebSockets.QWebSocketServer

    rcvdMsg = pyqtSignal(str)
    connection = pyqtSignal(bool)

    def __post_init__(self):
        super(QtServer, self).__init__()
        self.clients = []
        self.server = QtWebSockets.QWebSocketServer(self.parent.serverName(), self.parent.NonSecureMode, self.parent)

        if self.localhost_or_ipadress():
            self.listen = self.server.listen(QtNetwork.QHostAddress(QtNetwork.QHostAddress.LocalHost), self.port)
        else:
            self.listen =self.server.listen(QtNetwork.QHostAddress(self.ipaddress), self.port)

        if self.listen:
            log.info(
                f'Connected: {self.server.serverName()} : {self.server.serverAddress().toString()}:'
                f'{str(self.server.serverPort())}')
        else:
            log.info(f'QtServer error: {traceback.format_exc()}')
        self.server.setMaxPendingConnections(1)

        self.server.newConnection.connect(self.onNewConnection)
        print(f"Server listening{self.server.isListening()}")

    def log_the_correct_init(self):
        log.info(
            f'Connected: {self.server.serverName()} : {self.server.serverAddress().toString()}:'
            f'{str(self.server.serverPort())}')

    def localhost_or_ipadress(self):
        return self.ipaddress == "localhost"

    def onNewConnection(self):
        self.client_connection = self.server.nextPendingConnection()
        self.client_connection.textMessageReceived.connect(self.processTextMessage)
        self.client_connection.textFrameReceived.connect(self.processTextFrame)
        self.client_connection.binaryMessageReceived.connect(self.processBinaryMessage)
        self.client_connection.disconnected.connect(self.socketDisconnected)
        self.client_connection.ping()
        self.clients.append(self.client_connection)
        self.server.setMaxPendingConnections(0)

    def processTextFrame(self, frame, is_last_frame):
        print("in processTextFrame")
        print(f"\tFrame: {frame} ; is_last_frame: {is_last_frame}")

    def processTextMessage(self, message):
        if self.client_connection:
            print(message)
            self.rcvdMsg.emit(message)
            self.client_connection.sendTextMessage(message)

    def processBinaryMessage(self, message):
        if self.client_connection:
            self.client_connection.sendBinaryMessage(message)

    def socketDisconnected(self):
        if self.client_connection:
            self.clients.clear()
            self.client_connection.close()
            self.server.setMaxPendingConnections(1)
            self.client_connection.deleteLater()

