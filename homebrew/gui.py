import sys
import gui_auto
<<<<<<< HEAD
import gui_man
=======
import gui_man
import param
>>>>>>> 32e59bd73b1861ac49f59c95d6a4c80b24f20944
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Windows')
MainWindow = QtWidgets.QMainWindow()

def load(isAuto):
    if isAuto:
        ui = gui_auto.Ui_MainWindow()
    else:
        ui = gui_man.Ui_MainWindow()
    ui.setupUi(MainWindow)
    param.ui = ui
    MainWindow.show()
    app.exec_()
load(True)