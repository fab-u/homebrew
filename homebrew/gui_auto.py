# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Automatik.ui'ß
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import program
import motor
import tempControl
import tempSens
#import mainß

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.slider_settemp = QtWidgets.QSlider(self.centralwidget)
        self.slider_settemp.setGeometry(QtCore.QRect(150, 50, 381, 41))
        self.slider_settemp.setOrientation(QtCore.Qt.Horizontal)
        self.slider_settemp.setMaximum(100)
        self.slider_settemp.setObjectName("slider_settemp")
        self.slider_settemp.valueChanged.connect(self.tempsliderMoved)

        self.slider_setgeschw = QtWidgets.QSlider(self.centralwidget)
        self.slider_setgeschw.setGeometry(QtCore.QRect(150, 100, 381, 41))
        self.slider_setgeschw.setOrientation(QtCore.Qt.Horizontal)
        self.slider_setgeschw.setMaximum(10)
        self.slider_setgeschw.setObjectName("slider_setgeschw")
        self.slider_setgeschw.valueChanged.connect(self.speedsliderMoved)

        self.button_Step1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_Step1.setGeometry(QtCore.QRect(240, 10, 56, 21))
        self.button_Step1.setObjectName("button_Step1")
        self.button_Step1.clicked.connect(self.setstep1)

        self.button_Step2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_Step2.setGeometry(QtCore.QRect(300, 10, 56, 21))
        self.button_Step2.setObjectName("button_Step2")
        self.button_Step2.clicked.connect(self.setstep2)

        self.button_Step3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_Step3.setGeometry(QtCore.QRect(360, 10, 56, 21))
        self.button_Step3.setObjectName("button_Step3")
        self.button_Step3.clicked.connect(self.setstep3)

        self.button_Step4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_Step4.setGeometry(QtCore.QRect(420, 10, 56, 21))
        self.button_Step4.setObjectName("button_Step4")
        self.button_Step4.clicked.connect(self.setstep4)

        self.button_Step5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_Step5.setGeometry(QtCore.QRect(480, 10, 56, 21))
        self.button_Step5.setObjectName("button_Step5")
        self.button_Step5.clicked.connect(self.setstep5)

        self.label_show_step = QtWidgets.QLabel(self.centralwidget)
        self.label_show_step.setGeometry(QtCore.QRect(100, 250, 51, 16))
        self.label_show_step.setObjectName("label_show_step")
        self.lcd_show_step = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_show_step.setGeometry(QtCore.QRect(100, 270, 101, 51))
        self.lcd_show_step.setObjectName("lcd_show_step")
        self.checkbox_start_stopp = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_start_stopp.setGeometry(QtCore.QRect(30, 270, 71, 41))
        self.checkbox_start_stopp.setObjectName("checkbox_start_stopp")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 220, 800, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.settime = QtWidgets.QTimeEdit(self.centralwidget)
        self.settime.setGeometry(QtCore.QRect(190, 160, 101, 51))
        self.settime.setObjectName("settime")
        self.label_timer = QtWidgets.QLabel(self.centralwidget)
        self.label_timer.setGeometry(QtCore.QRect(190, 210, 61, 16))
        self.label_timer.setObjectName("label_timer")
        self.button_save_settings = QtWidgets.QPushButton(self.centralwidget)
        self.button_save_settings.setGeometry(QtCore.QRect(320, 160, 81, 31))
        self.button_save_settings.setObjectName("button_save_settings")
        self.label_step = QtWidgets.QLabel(self.centralwidget)
        self.label_step.setGeometry(QtCore.QRect(200, 10, 31, 16))
        self.label_step.setObjectName("label_step")
        self.lcd_show_dauer = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_show_dauer.setGeometry(QtCore.QRect(220, 270, 101, 51))
        self.lcd_show_dauer.setObjectName("lcd_show_dauer")
        self.label_show_dauer = QtWidgets.QLabel(self.centralwidget)
        self.label_show_dauer.setGeometry(QtCore.QRect(220, 250, 51, 16))
        self.label_show_dauer.setObjectName("label_show_dauer")
        self.lcd_show_solltemp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_show_solltemp.setGeometry(QtCore.QRect(570, 260, 81, 31))
        self.lcd_show_solltemp.setObjectName("lcd_show_solltemp")
        self.lcd_show_isttemp_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_show_isttemp_2.setGeometry(QtCore.QRect(570, 320, 81, 31))
        self.lcd_show_isttemp_2.setObjectName("lcd_show_isttemp_2")
        self.label_solltemp = QtWidgets.QLabel(self.centralwidget)
        self.label_solltemp.setGeometry(QtCore.QRect(570, 240, 71, 16))
        self.label_solltemp.setObjectName("label_solltemp")
        self.label_isttemp = QtWidgets.QLabel(self.centralwidget)
        self.label_isttemp.setGeometry(QtCore.QRect(570, 300, 61, 16))
        self.label_isttemp.setObjectName("label_isttemp")
        self.label_settemp = QtWidgets.QLabel(self.centralwidget)
        self.label_settemp.setGeometry(QtCore.QRect(90, 60, 51, 16))
        self.label_settemp.setObjectName("label_settemp")
        self.label_setgeschw = QtWidgets.QLabel(self.centralwidget)
        self.label_setgeschw.setGeometry(QtCore.QRect(90, 110, 51, 16))
        self.label_setgeschw.setObjectName("label_setgeschw")
        self.infobox_settings = QtWidgets.QTextEdit(self.centralwidget)
        self.infobox_settings.setGeometry(QtCore.QRect(570, 20, 201, 151))
        self.infobox_settings.setObjectName("infobox_settings")
        self.label_show_infobox = QtWidgets.QLabel(self.centralwidget)
        self.label_show_infobox.setGeometry(QtCore.QRect(350, 340, 51, 16))
        self.label_show_infobox.setObjectName("label_show_infobox")
        self.show_infobox = QtWidgets.QTextEdit(self.centralwidget)
        self.show_infobox.setGeometry(QtCore.QRect(350, 250, 181, 81))
        self.show_infobox.setObjectName("show_infobox")
        self.button_save_infobox = QtWidgets.QPushButton(self.centralwidget)
        self.button_save_infobox.setGeometry(QtCore.QRect(570, 180, 101, 31))
        self.button_save_infobox.setObjectName("button_save_infobox")
        self.comboBox_safedbier = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_safedbier.setGeometry(QtCore.QRect(10, 60, 53, 22))

        self.comboBox_safedbier.setObjectName("comboBox_safedbier")
        self.comboBox_safedbier.addItem("")
        self.comboBox_safedbier.addItem("")
        self.comboBox_safedbier.addItem("")
        self.comboBox_safedbier.addItem("")
        self.comboBox_safedbier.addItem("")

        self.label_setinfobox = QtWidgets.QLabel(self.centralwidget)
        self.label_setinfobox.setGeometry(QtCore.QRect(570, 0, 51, 16))
        self.label_setinfobox.setObjectName("label_setinfobox")

        self.button_manuelleeinstellungen = QtWidgets.QPushButton(self.centralwidget)
        self.button_manuelleeinstellungen.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.button_manuelleeinstellungen.setObjectName("button_manuelleeinstellungen")
        self.button_manuelleeinstellungen.clicked.connect(self.setMode)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuManuell = QtWidgets.QMenu(self.menubar)
        self.menuManuell.setObjectName("menuManuell")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuManuell.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_Step1.setText(_translate("MainWindow", "1"))
        self.button_Step2.setText(_translate("MainWindow", "2"))
        self.button_Step3.setText(_translate("MainWindow", "3"))
        self.button_Step4.setText(_translate("MainWindow", "4"))
        self.button_Step5.setText(_translate("MainWindow", "5"))
        self.label_show_step.setText(_translate("MainWindow", "Step"))
        self.checkbox_start_stopp.setText(_translate("MainWindow", "Start/Stopp"))
        self.label_timer.setText(_translate("MainWindow", "Timer (hh/mm)"))
        self.button_save_settings.setText(_translate("MainWindow", "Save Settings"))
        self.label_step.setText(_translate("MainWindow", "step:"))
        self.label_show_dauer.setText(_translate("MainWindow", "Dauer"))
        self.label_solltemp.setText(_translate("MainWindow", "Soll-Temperatur"))
        self.label_isttemp.setText(_translate("MainWindow", "Ist-Temperatur"))
        self.label_settemp.setText(_translate("MainWindow", "Temperatur"))
        self.label_setgeschw.setText(_translate("MainWindow", "Rührgeschw."))
        self.label_show_infobox.setText(_translate("MainWindow", "Infobox"))
        self.button_save_infobox.setText(_translate("MainWindow", "Save infobox settings"))
        self.comboBox_safedbier.setItemText(0, _translate("MainWindow", "Bier1"))
        self.comboBox_safedbier.setItemText(1, _translate("MainWindow", "Bier2"))
        self.comboBox_safedbier.setItemText(2, _translate("MainWindow", "Bier3"))
        self.comboBox_safedbier.setItemText(3, _translate("MainWindow", "Bier4"))
        self.comboBox_safedbier.setItemText(4, _translate("MainWindow", "Bier5"))
        self.label_setinfobox.setText(_translate("MainWindow", "set Infobox"))
        self.button_manuelleeinstellungen.setText(_translate("MainWindow", "Manuelle Einstellungen"))
        self.menuManuell.setTitle(_translate("MainWindow", "Automatik"))

    index = 0       #schrittzähler
    def setstep1(self):     #wenn step bearbeitet wird, buttonfarbe rot
        self.resetButtonColor()     #alle button-farben reset
        self.button_Step1.setStyleSheet("background-color: red")
        index = 0

    def setstep2(self):
        self.resetButtonColor()
        self.button_Step1.setStyleSheet("background-color: red")
        index = 1

    def setstep3(self):
        self.resetButtonColor()
        self.button_Step1.setStyleSheet("background-color: red")
        index = 2

    def setstep4(self):
        self.resetButtonColor()
        self.button_Step1.setStyleSheet("background-color: red")

    def setstep5(self):
        self.resetButtonColor()
        self.button_Step1.setStyleSheet("background-color: red")

    def safeSettings(self):
        self.button_Step1.setStyleSheet("background-color: red")

    def setMode(self):
        main.setMode(False)

    def resetButtonColor(self):
        self.button_Step1.setStyleSheet("background-color: grey")
        self.button_Step2.setStyleSheet("background-color: grey")
        self.button_Step3.setStyleSheet("background-color: grey")
        self.button_Step4.setStyleSheet("background-color: grey")
        self.button_Step5.setStyleSheet("background-color: grey")

    def tempsliderMoved(self):     #sliderwert in step speichern
        program.steps[index].heat = self.slider_settemp.value()

    def speedsliderMoved(self):
        program.steps[index].speed = self.slider_setgeschw.value()

def load():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())