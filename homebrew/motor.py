import RPi.GPIO as GPIO
import param

gpio = 18
frequencie = 200 

GPIO.setup(gpio, GPIO.OUT)
pwm = GPIO.PWM(gpio, frequencie)
pwm.start(0)

_speed = 0

def update():
    if not param.isOn:
        stop()

def restart():
    setSpeed(_speed)

#Stop motor
def stop():
    pwm.ChangeDutyCycle(0)

#Speed from 0 to 10
def setSpeed(speed):
    _speed = speed
    if param.isOn:
        pwm.ChangeDutyCycle(speed*10)