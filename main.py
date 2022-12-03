#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" Main program file from which it is launched. """
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
    send_msg_from_server = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        """
        Constructor of the GUI.
        Create the singletons and init the websocket server automatically.
        @:param parent: None
        """
        super().__init__(parent)
        # Init the server variables.
        self.server = None
        self.serverObject = None
        self.isDirectlyClose = None
        # Load ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Get the values of the interface
        self.uri = self.ui.lineEdit_ipaddress.text()
        self.port = int(self.ui.lineEdit_IP.text())
        # Create an instance of the singletons used.
        self.audio = AudioControl()
        self.creation_connection()
        self.system_status = SystemStatus()
        self.maintenance_state_task()
        # Connect signal button
        self.ui.change_btn.clicked.connect(self.is_client_valid)
        self.ui.label_led.setPixmap(QPixmap('qrc:/newPrefix/images/led-red-control-md.png'))
        # Get the current info devices connected and store the current volume when the app initialized.
        self.audio.gathering_info_audio_devices()
        self.old_volume = self.audio.current_volume_value()

    def maintenance_state_task(self) -> None:
        """
        Create an instance of MaintenanceState, a new QThread and move the object into the new thread.
        Create the connection between the signals and slots, and finally, start the thread.
        @:return: None
        """
        # Create an instance of the object which will be moved to a new QThread
        self.worker = MaintenanceState()
        self.maintenance_thread = QThread()
        self.worker.moveToThread(self.maintenance_thread)
        # Signals to kill QThread in the proper way
        self.worker.finished.connect(self.maintenance_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.maintenance_thread.finished.connect(self.maintenance_thread.deleteLater)
        # Custom signal and slots
        self.worker.check_is_client_is_valid.connect(self.is_client_valid)
        self.worker.check_volume_change.connect(self.control_current_volume)
        self.stop_maintenance_thread.connect(self.worker.set_stop_thread)
        self.send_signal_to_disconnect_client.connect(self.server.disconnect_client_from_server)
        # Init the thread
        self.maintenance_thread.started.connect(self.worker.run)
        self.maintenance_thread.start()

    def creation_connection(self):
        """
        Init the server using the data display in the GUI. Also connect signals and slots.
        @:return:
        """
        self.serverObject = QtWebSockets.QWebSocketServer('PyServer', QtWebSockets.QWebSocketServer.NonSecureMode)
        self.server = QtServer(ipaddress=self.uri, port=self.port, parent=self.serverObject)
        self.server.rcvdMsg.connect(self.data_received)
        self.server.on_close_connection_signal.connect(self.on_close_connection_routine)
        self.send_msg_from_server.connect(self.server.send_a_msg)

    @pyqtSlot(str)
    def data_received(self, rcvData) -> None:
        """
        Process the data received from the client.
        @:param rcvData: String with commands.
        @:return:None
        """
        # print(f'data recieved in Qt Server: {rcvData}')
        pass

    @pyqtSlot()
    def control_current_volume(self):
        """
        If volume change, we emit the new value and stored like old one, in order to compare
        the next change of volume.
        :return:
        """
        if self.old_volume != self.audio.current_volume_value():
            self.send_msg_from_server.emit(str(self.audio.current_volume_value()))
            log.info(f"Volume change: {self.audio.current_volume_value()}")
            self.old_volume = self.audio.current_volume_value()

    def is_client_valid(self) -> None:
        """
        As a security measure, if the client does not send a message with a specific structure immediately
        after connecting, the connection is terminated. If the message is correct,
        the valid connection routine is activated.
        @:return: None
        """
        if self.system_status.new_client_connected is True:
            if self.system_status.the_client_is_ is False:
                self.system_status.new_client_connected = False
                self.system_status.the_client_is_ = False
                self.send_signal_to_disconnect_client.emit()
            elif self.system_status.the_client_is_ is True:
                self.on_new_connection_routine()

    def on_new_connection_routine(self) -> None:
        """
        The flags are set to false for the next client, and information about the
        client that has connected is displayed on the screen.
        @:return: None
        """
        self.system_status.new_client_connected = False
        self.system_status.the_client_is_ = False
        self.ui.label_status.setText("Status connection: Connected")
        self.ui.label_ip_device_connected.setText(f'Ip device connected: {self.system_status.ip_device_connected}')
        self.ui.label_device_connection.setText(f'Device Connected: {self.system_status.name_device_connected}')
        self.ui.label_led.setPixmap(QPixmap(':/newPrefix/images/greenled15x15-md.png'))

    def on_close_connection_routine(self) -> None:
        """
        Change the info display in the screen when the client is disconnected.
        @:return: None
        """
        self.ui.label_status.setText("Status connection: Disconnected")
        self.ui.label_ip_device_connected.setText('Ip device connected: N/A')
        self.ui.label_device_connection.setText('Device Connected: N/A')
        self.ui.label_led.setPixmap(QPixmap(':/newPrefix/images/led-red-control-md.png'))

    def change_ip_routine(self):
        """
        In order to change the IP, it is necessary turn down the server and init again with the new uri and port
        @:return:
        """
        # TODO: finished this routine
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
    # Init the event-loop.
    sys.exit(app.exec())
