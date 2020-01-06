# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_manuell.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import tempSens
import tempControl
import motor
import param

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slider_setgeschw = QtWidgets.QSlider(self.centralwidget)
        self.slider_setgeschw.setGeometry(QtCore.QRect(180, 65, 381, 81))
        self.slider_setgeschw.setOrientation(QtCore.Qt.Horizontal)
        self.slider_setgeschw.setMaximum(10)
        self.slider_setgeschw.setObjectName("slider_setgeschw")

        self.slider_settemp = QtWidgets.QSlider(self.centralwidget)
        self.slider_settemp.setGeometry(QtCore.QRect(180, 170, 381, 81))
        self.slider_settemp.setOrientation(QtCore.Qt.Horizontal)
        self.slider_settemp.setObjectName("slider_settemp")
        self.slider_settemp.setMaximum(100)
        self.slider_settemp.valueChanged.connect(self.setTemp)

        self.button_automatik = QtWidgets.QPushButton(self.centralwidget)
        self.button_automatik.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.button_automatik.setObjectName("button_automatik")
        self.button_automatik.clicked.connect(self.setAutomatic)

        self.label_setgeschw = QtWidgets.QLabel(self.centralwidget)
        self.label_setgeschw.setGeometry(QtCore.QRect(90, 100, 81, 21))
        self.label_setgeschw.setObjectName("label_setgeschw")

        self.label_settemp = QtWidgets.QLabel(self.centralwidget)
        self.label_settemp.setGeometry(QtCore.QRect(90, 180, 81, 21))
        self.label_settemp.setObjectName("label_settemp")

        self.lcd_showsolltemp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_showsolltemp.setGeometry(QtCore.QRect(30, 300, 111, 51))
        self.lcd_showsolltemp.setObjectName("lcd_showsolltemp")
        self.lcd_showisttemp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_showisttemp.setGeometry(QtCore.QRect(200, 300, 111, 51))
        self.lcd_showisttemp.setObjectName("lcd_showisttemp")

        self.label_solltemp = QtWidgets.QLabel(self.centralwidget)
        self.label_solltemp.setGeometry(QtCore.QRect(30, 280, 71, 16))
        self.label_solltemp.setObjectName("label_solltemp")

        self.label_isttemp = QtWidgets.QLabel(self.centralwidget)
        self.label_isttemp.setGeometry(QtCore.QRect(200, 280, 71, 16))
        self.label_isttemp.setObjectName("label_isttemp")

        self.button_start_manuell = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_manuell.setGeometry(QtCore.QRect(440, 280, 181, 71))
        self.button_start_manuell.setObjectName("button_start_manuell")
        self.button_start_manuell.clicked.connect(self.start)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")

        self.menumanuell = QtWidgets.QMenu(self.menubar)
        self.menumanuell.setObjectName("menumanuell")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menumanuell.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_automatik.setText(_translate("MainWindow", "automatik"))
        self.label_setgeschw.setText(_translate("MainWindow", "Rührgeschwindigkeit"))
        self.label_settemp.setText(_translate("MainWindow", "Temperatur"))
        self.label_solltemp.setText(_translate("MainWindow", "Soll-temperatur"))
        self.label_isttemp.setText(_translate("MainWindow", "Ist-temperatur"))
        self.button_start_manuell.setText(_translate("MainWindow", "Start/Stopp"))
        self.menumanuell.setTitle(_translate("MainWindow", "manuell"))

    def start(self):
        if param.isOn:
            param.isOn = False
            tempControl.off()
            self.button_start_manuell.setText("ON")
        else:
            param.isOn = True
            self.button_start_manuell.setText("OFF")

    def setAutomatic(self):
        param.setMode(True)

    def setTemp(self):
        tempControl.setTemp(self.slider_settemp.value())
        self.lcd_showsolltemp.display(self.slider_settemp.value())

    def setSpeed(self):
        motor.setSpeed(self.slider_setgeschw.value())

def load():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
