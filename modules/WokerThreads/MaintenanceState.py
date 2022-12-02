#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" TODO: Fill"""
# ---------------------------------------------------------------------------
import logging
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal, QObject
from modules.Utils.SystemStatus import SystemStatus


class MaintenanceState(QObject):
    """

    """
    finished = pyqtSignal()
    check_is_client_is_valid = pyqtSignal()

    def __init__(self):
        super(MaintenanceState, self).__init__()
        logging.info("Init del hilo")
        self._stop_flag = True
        self.system_status = SystemStatus()

    def __del__(self):
        """

        :return:
        """
        pass

    @property
    def stop_thread(self):
        return self._stop_flag

    @stop_thread.setter
    def stop_thread(self, new_value):
        self._stop_flag = new_value

    @pyqtSlot()
    def set_stop_thread(self):
        self._stop_flag = False

    def run(self) -> None:
        while self._stop_flag:

            if self.system_status.new_client_connected is True:
                self.check_is_client_is_valid.emit()

            # self.finished.emit()

            QThread.msleep(3000)
