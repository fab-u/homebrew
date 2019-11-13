#raspi lib
import RPi.GPIO as GPIO

#user lib
import motor
import gpio
import program
import tempControll
import tempSens

#initialize system
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

motor.init(2)

motor.start(50)


#m = motor(2000)
#m.start(50)
