# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wsQtServer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 651)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 52, 731, 431))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"background-color : rgb(255, 255, 200)")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(17, 40, 691, 80))
        font2 = QFont()
        font2.setBold(True)
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"background-color :rgb(240, 240, 255)")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(12, 23, 50, 16))
        self.le_cliOutSol1 = QLineEdit(self.groupBox)
        self.le_cliOutSol1.setObjectName(u"le_cliOutSol1")
        self.le_cliOutSol1.setGeometry(QRect(64, 20, 20, 20))
        self.le_cliOutSol1.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliOutSol2 = QLineEdit(self.groupBox)
        self.le_cliOutSol2.setObjectName(u"le_cliOutSol2")
        self.le_cliOutSol2.setGeometry(QRect(150, 20, 20, 20))
        self.le_cliOutSol2.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(98, 23, 50, 16))
        self.le_cliOutSol3 = QLineEdit(self.groupBox)
        self.le_cliOutSol3.setObjectName(u"le_cliOutSol3")
        self.le_cliOutSol3.setGeometry(QRect(240, 20, 20, 20))
        self.le_cliOutSol3.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(188, 23, 50, 16))
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 53, 110, 16))
        self.le_cliOutSensorPump = QLineEdit(self.groupBox)
        self.le_cliOutSensorPump.setObjectName(u"le_cliOutSensorPump")
        self.le_cliOutSensorPump.setGeometry(QRect(290, 50, 20, 20))
        self.le_cliOutSensorPump.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliOutSamplePump = QLineEdit(self.groupBox)
        self.le_cliOutSamplePump.setObjectName(u"le_cliOutSamplePump")
        self.le_cliOutSamplePump.setGeometry(QRect(123, 50, 20, 20))
        self.le_cliOutSamplePump.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(12, 53, 110, 16))
        self.le_cliOutFan = QLineEdit(self.groupBox)
        self.le_cliOutFan.setObjectName(u"le_cliOutFan")
        self.le_cliOutFan.setGeometry(QRect(330, 20, 20, 20))
        self.le_cliOutFan.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(278, 23, 50, 16))
        self.le_cliOutHeat = QLineEdit(self.groupBox)
        self.le_cliOutHeat.setObjectName(u"le_cliOutHeat")
        self.le_cliOutHeat.setGeometry(QRect(420, 20, 20, 20))
        self.le_cliOutHeat.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(368, 23, 50, 16))
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(18, 140, 691, 111))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color :rgb(240, 240, 255)")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(586, 23, 50, 16))
        self.le_cliInTempEx = QLineEdit(self.groupBox_2)
        self.le_cliInTempEx.setObjectName(u"le_cliInTempEx")
        self.le_cliInTempEx.setGeometry(QRect(628, 23, 50, 20))
        self.le_cliInTempEx.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(12, 51, 50, 16))
        self.le_cliInHumEx = QLineEdit(self.groupBox_2)
        self.le_cliInHumEx.setObjectName(u"le_cliInHumEx")
        self.le_cliInHumEx.setGeometry(QRect(58, 51, 50, 20))
        self.le_cliInHumEx.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliInHumIn = QLineEdit(self.groupBox_2)
        self.le_cliInHumIn.setObjectName(u"le_cliInHumIn")
        self.le_cliInHumIn.setGeometry(QRect(278, 51, 50, 20))
        self.le_cliInHumIn.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(126, 51, 50, 16))
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(232, 51, 50, 16))
        self.le_cliInTempIn = QLineEdit(self.groupBox_2)
        self.le_cliInTempIn.setObjectName(u"le_cliInTempIn")
        self.le_cliInTempIn.setGeometry(QRect(168, 51, 50, 20))
        self.le_cliInTempIn.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliInStLimit = QLineEdit(self.groupBox_2)
        self.le_cliInStLimit.setObjectName(u"le_cliInStLimit")
        self.le_cliInStLimit.setGeometry(QRect(303, 23, 20, 20))
        self.le_cliInStLimit.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(11, 23, 50, 16))
        self.le_cliInBtnSample = QLineEdit(self.groupBox_2)
        self.le_cliInBtnSample.setObjectName(u"le_cliInBtnSample")
        self.le_cliInBtnSample.setGeometry(QRect(147, 23, 20, 20))
        self.le_cliInBtnSample.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(179, 23, 50, 16))
        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(89, 23, 60, 16))
        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(259, 23, 50, 16))
        self.le_cliInBtnClean = QLineEdit(self.groupBox_2)
        self.le_cliInBtnClean.setObjectName(u"le_cliInBtnClean")
        self.le_cliInBtnClean.setGeometry(QRect(226, 23, 20, 20))
        self.le_cliInBtnClean.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliInBtnStart = QLineEdit(self.groupBox_2)
        self.le_cliInBtnStart.setObjectName(u"le_cliInBtnStart")
        self.le_cliInBtnStart.setGeometry(QRect(54, 23, 20, 20))
        self.le_cliInBtnStart.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliInStDoor1 = QLineEdit(self.groupBox_2)
        self.le_cliInStDoor1.setObjectName(u"le_cliInStDoor1")
        self.le_cliInStDoor1.setGeometry(QRect(386, 23, 20, 20))
        self.le_cliInStDoor1.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(336, 23, 50, 16))
        self.le_cliInStDoor2 = QLineEdit(self.groupBox_2)
        self.le_cliInStDoor2.setObjectName(u"le_cliInStDoor2")
        self.le_cliInStDoor2.setGeometry(QRect(468, 23, 20, 20))
        self.le_cliInStDoor2.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(418, 23, 50, 16))
        self.le_cliInStPump = QLineEdit(self.groupBox_2)
        self.le_cliInStPump.setObjectName(u"le_cliInStPump")
        self.le_cliInStPump.setGeometry(QRect(553, 22, 20, 20))
        self.le_cliInStPump.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(502, 22, 50, 16))
        self.le_cliInAdcAngle = QLineEdit(self.groupBox_2)
        self.le_cliInAdcAngle.setObjectName(u"le_cliInAdcAngle")
        self.le_cliInAdcAngle.setGeometry(QRect(388, 51, 50, 20))
        self.le_cliInAdcAngle.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(334, 51, 50, 16))
        self.le_cliInCntAirVel = QLineEdit(self.groupBox_2)
        self.le_cliInCntAirVel.setObjectName(u"le_cliInCntAirVel")
        self.le_cliInCntAirVel.setGeometry(QRect(498, 51, 50, 20))
        self.le_cliInCntAirVel.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(447, 51, 50, 16))
        self.le_cliInAdcOvpVolt = QLineEdit(self.groupBox_2)
        self.le_cliInAdcOvpVolt.setObjectName(u"le_cliInAdcOvpVolt")
        self.le_cliInAdcOvpVolt.setGeometry(QRect(609, 51, 50, 20))
        self.le_cliInAdcOvpVolt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(558, 51, 50, 16))
        self.le_cliInAdcPreVolt = QLineEdit(self.groupBox_2)
        self.le_cliInAdcPreVolt.setObjectName(u"le_cliInAdcPreVolt")
        self.le_cliInAdcPreVolt.setGeometry(QRect(62, 80, 50, 20))
        self.le_cliInAdcPreVolt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(11, 80, 50, 16))
        self.le_cliInAdcOdorVolt = QLineEdit(self.groupBox_2)
        self.le_cliInAdcOdorVolt.setObjectName(u"le_cliInAdcOdorVolt")
        self.le_cliInAdcOdorVolt.setGeometry(QRect(175, 80, 50, 20))
        self.le_cliInAdcOdorVolt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(122, 80, 50, 16))
        self.le_cliInAdcH2cVolt = QLineEdit(self.groupBox_2)
        self.le_cliInAdcH2cVolt.setObjectName(u"le_cliInAdcH2cVolt")
        self.le_cliInAdcH2cVolt.setGeometry(QRect(283, 80, 50, 20))
        self.le_cliInAdcH2cVolt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(232, 80, 50, 16))
        self.le_cliInAdcNh3Volt = QLineEdit(self.groupBox_2)
        self.le_cliInAdcNh3Volt.setObjectName(u"le_cliInAdcNh3Volt")
        self.le_cliInAdcNh3Volt.setGeometry(QRect(390, 80, 50, 20))
        self.le_cliInAdcNh3Volt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(339, 80, 50, 16))
        self.le_cliInAdcVocVolt = QLineEdit(self.groupBox_2)
        self.le_cliInAdcVocVolt.setObjectName(u"le_cliInAdcVocVolt")
        self.le_cliInAdcVocVolt.setGeometry(QRect(500, 78, 50, 20))
        self.le_cliInAdcVocVolt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_32 = QLabel(self.groupBox_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(449, 78, 50, 16))
        self.label_14.raise_()
        self.le_cliInTempEx.raise_()
        self.label_15.raise_()
        self.le_cliInHumEx.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.le_cliInTempIn.raise_()
        self.le_cliInHumIn.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.le_cliInBtnClean.raise_()
        self.le_cliInBtnStart.raise_()
        self.le_cliInStLimit.raise_()
        self.le_cliInBtnSample.raise_()
        self.label_22.raise_()
        self.le_cliInStDoor1.raise_()
        self.le_cliInStDoor2.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.le_cliInStPump.raise_()
        self.le_cliInAdcAngle.raise_()
        self.label_25.raise_()
        self.le_cliInCntAirVel.raise_()
        self.label_26.raise_()
        self.le_cliInAdcOvpVolt.raise_()
        self.label_27.raise_()
        self.le_cliInAdcPreVolt.raise_()
        self.label_28.raise_()
        self.le_cliInAdcOdorVolt.raise_()
        self.label_29.raise_()
        self.le_cliInAdcH2cVolt.raise_()
        self.label_30.raise_()
        self.le_cliInAdcNh3Volt.raise_()
        self.label_31.raise_()
        self.le_cliInAdcVocVolt.raise_()
        self.label_32.raise_()
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(18, 270, 691, 111))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"background-color :rgb(240, 240, 255)")
        self.le_cliSysSenDt = QLineEdit(self.groupBox_3)
        self.le_cliSysSenDt.setObjectName(u"le_cliSysSenDt")
        self.le_cliSysSenDt.setGeometry(QRect(260, 24, 131, 20))
        self.le_cliSysSenDt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(200, 26, 61, 16))
        self.label_34 = QLabel(self.groupBox_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(400, 24, 61, 16))
        self.le_cliSysFwVersion = QLineEdit(self.groupBox_3)
        self.le_cliSysFwVersion.setObjectName(u"le_cliSysFwVersion")
        self.le_cliSysFwVersion.setGeometry(QRect(460, 24, 61, 20))
        self.le_cliSysFwVersion.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_35 = QLabel(self.groupBox_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(530, 24, 61, 16))
        self.le_cliSysCntProc = QLineEdit(self.groupBox_3)
        self.le_cliSysCntProc.setObjectName(u"le_cliSysCntProc")
        self.le_cliSysCntProc.setGeometry(QRect(594, 24, 71, 20))
        self.le_cliSysCntProc.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliSysRsvDt = QLineEdit(self.groupBox_3)
        self.le_cliSysRsvDt.setObjectName(u"le_cliSysRsvDt")
        self.le_cliSysRsvDt.setGeometry(QRect(262, 54, 131, 20))
        self.le_cliSysRsvDt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_36 = QLabel(self.groupBox_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(210, 56, 51, 16))
        self.label_37 = QLabel(self.groupBox_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(420, 54, 61, 16))
        self.le_cliSysRsvProc = QLineEdit(self.groupBox_3)
        self.le_cliSysRsvProc.setObjectName(u"le_cliSysRsvProc")
        self.le_cliSysRsvProc.setGeometry(QRect(470, 54, 20, 20))
        self.le_cliSysRsvProc.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.le_cliSysAutoLevel = QLineEdit(self.groupBox_3)
        self.le_cliSysAutoLevel.setObjectName(u"le_cliSysAutoLevel")
        self.le_cliSysAutoLevel.setGeometry(QRect(143, 53, 50, 20))
        self.le_cliSysAutoLevel.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_38 = QLabel(self.groupBox_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(95, 53, 51, 16))
        self.label_39 = QLabel(self.groupBox_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(11, 53, 51, 16))
        self.le_cliSysAutoPrc = QLineEdit(self.groupBox_3)
        self.le_cliSysAutoPrc.setObjectName(u"le_cliSysAutoPrc")
        self.le_cliSysAutoPrc.setGeometry(QRect(61, 53, 20, 20))
        self.le_cliSysAutoPrc.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_40 = QLabel(self.groupBox_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(7, 84, 101, 16))
        self.lineEdit_42 = QLineEdit(self.groupBox_3)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setGeometry(QRect(80, 24, 111, 20))
        self.lineEdit_42.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_43 = QLabel(self.groupBox_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(9, 26, 71, 16))
        self.le_cliSysSampleStartDt = QLineEdit(self.groupBox_3)
        self.le_cliSysSampleStartDt.setObjectName(u"le_cliSysSampleStartDt")
        self.le_cliSysSampleStartDt.setGeometry(QRect(103, 82, 131, 20))
        self.le_cliSysSampleStartDt.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_45 = QLabel(self.groupBox_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(243, 83, 91, 16))
        self.le_cliSysSampleStartDt_2 = QLineEdit(self.groupBox_3)
        self.le_cliSysSampleStartDt_2.setObjectName(u"le_cliSysSampleStartDt_2")
        self.le_cliSysSampleStartDt_2.setGeometry(QRect(334, 81, 61, 20))
        self.le_cliSysSampleStartDt_2.setStyleSheet(u"background-color:rgb(251, 254, 255)")
        self.label_33.raise_()
        self.label_34.raise_()
        self.le_cliSysSenDt.raise_()
        self.le_cliSysFwVersion.raise_()
        self.label_35.raise_()
        self.le_cliSysCntProc.raise_()
        self.label_36.raise_()
        self.le_cliSysRsvDt.raise_()
        self.label_37.raise_()
        self.le_cliSysRsvProc.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.le_cliSysAutoPrc.raise_()
        self.label_40.raise_()
        self.label_43.raise_()
        self.le_cliSysAutoLevel.raise_()
        self.lineEdit_42.raise_()
        self.le_cliSysSampleStartDt.raise_()
        self.label_45.raise_()
        self.le_cliSysSampleStartDt_2.raise_()
        self.label_42 = QLabel(self.tab)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(460, 11, 121, 20))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_42.setFont(font3)
        self.label_44 = QLabel(self.tab)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(572, 10, 131, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.plainTextEdit = QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 40, 681, 141))
        self.plainTextEdit.setStyleSheet(u"background-color :rgb(232, 255, 220)")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 14, 85, 16))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_5.setFont(font4)
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(600, 195, 90, 31))
        self.pushButton_7.setFont(font4)
        self.pushButton_7.setStyleSheet(u"QPushButton { background-color: rgb(227, 227, 143);\n"
"border-radius: 12px;\n"
"border: 3px solid rgb(43, 93, 153);}\n"
"QPushButton:pressed { background-color: rgb(200, 200, 100);\n"
"border-radius: 12px;\n"
"border: 3px solid rgb(43, 93, 153); }")
        self.lineEdit_40 = QLineEdit(self.tab_2)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setGeometry(QRect(448, 195, 141, 31))
        font5 = QFont()
        font5.setPointSize(12)
        self.lineEdit_40.setFont(font5)
        self.lineEdit_40.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 3px solid rgb(60, 60, 60)")
        self.label_41 = QLabel(self.tab_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(299, 201, 151, 16))
        self.label_41.setFont(font4)
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 261, 345, 101))
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 85, 16))
        self.label_3.setFont(font4)
        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(246, 54, 90, 31))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"QPushButton { background-color: rgb(227, 227, 143);\n"
"border-radius: 12px;\n"
"border: 3px solid rgb(43, 93, 153);}\n"
"QPushButton:pressed { background-color: rgb(200, 200, 100);\n"
"border-radius: 12px;\n"
"border: 3px solid rgb(43, 93, 153); }")
        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(96, 54, 141, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 3px solid rgb(60, 60, 60)")
        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(12, 12, 91, 20))
        font6 = QFont()
        font6.setPointSize(11)
        self.checkBox.setFont(font6)
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(380, 260, 318, 101))
        self.pushButton_4 = QPushButton(self.groupBox_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(218, 53, 90, 31))
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"QPushButton { background-color: rgb(227, 227, 143);\n"
"border-radius: 12px;\n"
"border: 3px solid rgb(43, 93, 153);}\n"
"QPushButton:pressed { background-color: rgb(200, 200, 100);\n"
"border-radius: 12px;\n"
"border: 3px solid rgb(43, 93, 153); }")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 59, 85, 16))
        self.label_4.setFont(font4)
        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(98, 53, 111, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 3px solid rgb(60, 60, 60)")
        self.checkBox_2 = QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 11, 91, 20))
        self.checkBox_2.setFont(font6)
        self.tabWidget.addTab(self.tab_2, "")
        self.plainTextEdit.raise_()
        self.label_5.raise_()
        self.pushButton_7.raise_()
        self.label_41.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.lineEdit_40.raise_()
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(770, 210, 80, 31))
        self.pushButton.setFont(font4)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(770, 280, 80, 31))
        self.pushButton_2.setFont(font4)
        self.le_srvIpAddr = QLineEdit(self.centralwidget)
        self.le_srvIpAddr.setObjectName(u"le_srvIpAddr")
        self.le_srvIpAddr.setGeometry(QRect(322, 20, 121, 22))
        self.le_srvDateTime = QLineEdit(self.centralwidget)
        self.le_srvDateTime.setObjectName(u"le_srvDateTime")
        self.le_srvDateTime.setGeometry(QRect(590, 20, 161, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 151, 16))
        self.label.setFont(font4)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 20, 111, 16))
        self.label_2.setFont(font4)
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(20, 524, 821, 110))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 500, 85, 16))
        self.label_6.setFont(font4)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(770, 350, 80, 31))
        self.pushButton_8.setFont(font4)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(770, 420, 80, 31))
        self.pushButton_9.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Websocket-Server", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SolOut1:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SolOut2:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SolOut3:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sensor-Pump-Out:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sample-Pump-Out:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"FanOut:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"HeatOut:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"exTmp:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"exHum:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"inTmp:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"inHum:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"btStart:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"btClean:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"btSample:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"limitSt:", None))
        self.le_cliInStDoor1.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"door1St:", None))
        self.le_cliInStDoor2.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"door2St:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"pumpSt:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"dirAngle:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"aVelCnt:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"ovpVolt:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"preVolt:", None))
        self.le_cliInAdcOdorVolt.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"odorVolt:", None))
        self.le_cliInAdcH2cVolt.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"h2sVolt:", None))
        self.le_cliInAdcNh3Volt.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"nh3Volt:", None))
        self.le_cliInAdcVocVolt.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"vocVolt:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"System", None))
        self.le_cliSysSenDt.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"sensingDt:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"fwVersion:", None))
        self.le_cliSysFwVersion.setText(QCoreApplication.translate("MainWindow", u"V1.0001", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"cntProcess:", None))
        self.le_cliSysCntProc.setText("")
        self.le_cliSysRsvDt.setText(QCoreApplication.translate("MainWindow", u"2021-07-26 11:35:43", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"rsvedDt:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"rsvedPrc:", None))
        self.le_cliSysRsvProc.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"autoLev:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"autoPrc:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"sampleStartTime:", None))
        self.lineEdit_42.setText(QCoreApplication.translate("MainWindow", u"dc:a6:32:7b:24:b4", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"devMacAdd:", None))
        self.le_cliSysSampleStartDt.setText(QCoreApplication.translate("MainWindow", u"2021-07-26 11:35:43", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"sampleLabTime:", None))
        self.le_cliSysSampleStartDt_2.setText(QCoreApplication.translate("MainWindow", u"11:35:43", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"from Client-IP:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700; color:#0000ff;\">192.168.123.111</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Json Data", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.lineEdit_40.setText(QCoreApplication.translate("MainWindow", u"192.168.123.148", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"device IP Address :", None))
        self.groupBox_4.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc57d \uc2dc\uac04 :", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc57d \uc124\uc815", None))
        self.groupBox_5.setTitle("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc13c\uc2f1 \ub808\ubca8 :", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub3d9 \uc124\uc815", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sample", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.le_srvIpAddr.setText(QCoreApplication.translate("MainWindow", u"192.168.123.117", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Server IP Address :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date & Time :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Rcv Data", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Print", None))
    # retranslateUi

