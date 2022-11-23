import sys

from PyQt5.QtWebSockets import QWebSocket
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5.QtGui import QScreen
from modules.GUI.ui_form import Ui_MainWindow
from modules.Comm.WebSocket.Web_Socket_Server import QtServer
from PyQt5 import QtWebSockets, QtNetwork
from PyQt5.QtCore import QObject, pyqtSignal
from dataclasses import dataclass


@dataclass
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.server = None
        self.serverObject = None
        self.isDirectlyClose = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.uri = f"ws//:{self.ui.textEdit_IP_Address}"
        self.port = int(self.ui.textEdit_Port.toPlainText())
        self.creation_connection()

    def creation_connection(self):
        self.serverObject = QtWebSockets.QWebSocketServer('PyServer', QtWebSockets.QWebSocketServer.NonSecureMode)
        self.server = QtServer(ipaddress=self.uri, port=self.port, parent=self.serverObject)
        self.server.rcvdMsg.connect(self.printRcv)
        # Deploy the server

    @pyqtSlot(str)
    def printRcv(self, rcvData):
        print(f'data recieved in Qt Server: {rcvData}')

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
