#raspi lib
import RPi.GPIO as GPIO

#general GPIO Settings
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#user lib
import motor
import gpio
import program
import tempControl
import tempSens
import gui, gui_auto, gui_man

#std lib
import threading

#global variables
isOn = False

#local used variables
_isAuto = False
_loopDelayTimer = 2.0

#define methods
def _mainLoop():
    threading.Timer(_loopDelayTimer, _mainLoop).start()

    if _isAuto:
        if isOn:
            program.update()
    if(isOn):
        tempControl.update(tempSens.get())
    else:
        tempControl.off()

def setMode(isAuto):
    _isAuto = isAuto
    gui.load(isAuto)

#initialisation script
tempControl.init()

_mainLoop() #start mainLoop
gui.load(False) #load manual user interface
