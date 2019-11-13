import RPi.GPIO as GPIO
from motor import motor
import gpio

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

gpio.test()

#m = motor(2000)
#m.start(50)
