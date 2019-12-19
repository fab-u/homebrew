#raspi lib
import RPi.GPIO as GPIO

#user lib
import motor
import gpio
import program
import tempControl
import tempSens
import gui, gui_auto, gui_man

#local variables
isOn = False
_isAuto = False

#general GPIO Settings
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#initialize system
gui.load(False) #load manual user interface

#main loop
while True:
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