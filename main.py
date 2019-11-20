#raspi lib
import RPi.GPIO as GPIO

#General GPIO Settings
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#User lib
import motor
import gpio
import program
import tempControll
import tempSens

#initialize system
