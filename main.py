import RPi.GPIO as GPIO
import motor.motor as motor

GPIO.setmode(GPIO.BCM)

m = motor(2000)
m.start(50)