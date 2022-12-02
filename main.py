#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" MAIN FILE"""
# ---------------------------------------------------------------------------
import sys
from dataclasses import dataclass
import logging
# ---------------------------------------------------------------------------
from PyQt5 import QtWebSockets
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from PyQt5.QtGui import QScreen, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
# ---------------------------------------------------------------------------
from modules.Comm.WebSocket.Web_Socket_Server import QtServer
from modules.GUI.ui_form import Ui_MainWindow
from modules.WokerThreads.MaintenanceState import MaintenanceState
from modules.Utils.SystemStatus import SystemStatus
from modules.Audio.ControlAudio import AudioControl

# ----------------------SET UP LOGGING MODULE -------------------------------
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------


@dataclass
class MainWindow(QMainWindow):
    send_signal_to_disconnect_client = pyqtSignal()
    stop_maintenance_thread = pyqtSignal()
    send_audio_devices_lists = pyqtSignal()

    def __init__(self, parent=None):
        """

        :param parent:
        """
        super().__init__(parent)
        self.server = None
        self.serverObject = None
        self.isDirectlyClose = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.uri = self.ui.lineEdit_ipaddress.text()
        self.port = int(self.ui.lineEdit_IP.text())
        self.creation_connection()
        self.system_status = SystemStatus()
        self.ui.change_btn.clicked.connect(self.is_client_valid)
        self.maintenance_state_task()
        self.ui.label_led.setPixmap(QPixmap(':/newPrefix/images/led-red-control-md.png'))
        self.audio = AudioControl().gathering_info_audio_devices()

    def maintenance_state_task(self):
        """
        :return:
        """
        self.worker = MaintenanceState()
        self.maintenance_thread = QThread()
        self.worker.moveToThread(self.maintenance_thread)
        " Signals to kill QThread in the proper way"
        self.worker.finished.connect(self.maintenance_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.maintenance_thread.finished.connect(self.maintenance_thread.deleteLater)
        " Custom signal and slots"
        self.worker.finished.connect(self.testing_thread)
        self.worker.check_is_client_is_valid.connect(self.is_client_valid)
        self.stop_maintenance_thread.connect(self.worker.set_stop_thread)
        self.send_signal_to_disconnect_client.connect(self.server.disconnect_client_from_server)
        " Init the thread"
        self.maintenance_thread.started.connect(self.worker.run)
        self.maintenance_thread.start()

    def creation_connection(self):
        """

        :return:
        """
        self.serverObject = QtWebSockets.QWebSocketServer('PyServer', QtWebSockets.QWebSocketServer.NonSecureMode)
        self.server = QtServer(ipaddress=self.uri, port=self.port, parent=self.serverObject)
        self.server.rcvdMsg.connect(self.print_rcv)
        self.server.on_close_connection_signal.connect(self.on_close_connection_routine)

    @pyqtSlot(str)
    def print_rcv(self, rcvData):
        # print(f'data recieved in Qt Server: {rcvData}')
        pass

    @pyqtSlot()
    def testing_thread(self):
        logging.info("recibiendo señal del hilo")

    def is_client_valid(self):
        if self.system_status.new_client_connected is True:
            if self.system_status.the_client_is_ is False:
                self.system_status.new_client_connected = False
                self.system_status.the_client_is_ = False
                self.send_signal_to_disconnect_client.emit()
            elif self.system_status.the_client_is_ is True:
                self.on_new_connection_routine()

    def on_new_connection_routine(self):
        self.system_status.new_client_connected = False
        self.system_status.the_client_is_ = False
        self.ui.label_status.setText("Status connection: Connected")
        self.ui.label_ip_device_connected.setText(f'Ip device connected: {self.system_status.ip_device_connected}')
        self.ui.label_device_connection.setText(f'Device Connected: {self.system_status.name_device_connected}')
        self.ui.label_led.setPixmap(QPixmap(':/newPrefix/images/greenled15x15-md.png'))

    def on_close_connection_routine(self):
        self.ui.label_status.setText("Status connection: Disconnected")
        self.ui.label_ip_device_connected.setText('Ip device connected: N/A')
        self.ui.label_device_connection.setText('Device Connected: N/A')
        self.ui.label_led.setPixmap(QPixmap(':/newPrefix/images/led-red-control-md.png'))

    def change_ip_routine(self):
        self.on_close_connection_routine()
        QThread.msleep(200)
        self.send_signal_to_disconnect_client.emit()

    # --------------------------------------------------------
    # Event-> to close the window
    # --------------------------------------------------------

    def close(self):
        """
        Close all the QWidgets and set self.isDirectlyClose = True.

        @return: QMainWindow.close
        """
        for childQWidget in self.findChildren(QWidget):
            childQWidget.close()
        self.isDirectlyClose = True
        for name in dir():
            del globals()[name]
        return QMainWindow.close(self)

    def closeEvent(self, eventQCloseEvent):
        """
        Close the windows and terminate all the connections before close.

        @param eventQCloseEvent: Event to allow the user decided if the MainWindow(for hence the program) is going
                                  to be closed or not.
        @type eventQCloseEvent: QEvent
        """
        if self.isDirectlyClose:
            eventQCloseEvent.accept()
        else:
            answer = QMessageBox.question(
                self,
                'Close the program?',
                'Are you sure?',
                QMessageBox.Yes,
                QMessageBox.No)
            if (answer == QMessageBox.Yes) or (self.isDirectlyClose is True):
                eventQCloseEvent.accept()
                # self.serverObject.connect()
                sys.exit(0)
            else:
                eventQCloseEvent.ignore()


if __name__ == "__main__":
    # Init the application
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    # Center the widget
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = widget.frameGeometry()
    geo.moveCenter(center)
    widget.move(geo.topLeft())
    # Init the loop
    sys.exit(app.exec())
