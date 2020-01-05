import sys
import gui_auto
#import gui_man
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
    MainWindow.show()
    app.exec_()
load(True)