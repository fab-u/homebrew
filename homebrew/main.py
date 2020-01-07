#raspi lib
import RPi.GPIO as GPIO

#general GPIO Settings
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#user lib
import param
import motor
import gpio
import program
import tempControl
import tempSens
import gui
import gui_auto
import gui_man

#std lib
import threading

#local used variables
_loopDelayTimer = 2.0

#define methods
def _mainLoop():
    threading.Timer(_loopDelayTimer, _mainLoop).start()

    if param.isAuto:
        if param.isOn:
            program.update()
    if(param.isOn):
        tempControl.update(tempSens.get())
    else:
        tempControl.off()
        motor.update()

#initialisation script
tempControl.init()

_mainLoop() #start mainLoop
gui.load(False) #load manual user interface
