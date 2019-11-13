import RPi.GPIO as GPIO
from motor import motor

GPIO.setmode(GPIO.BCM)

m = motor(2000)
m.start(50)