import RPi.GPIO as GPIO

def init(frequencie):
    pwm = GPIO.PWM(13, frequencie)

def start(speed):
    pwm.start(speed)
    
def stop():
    pwm.stop()

def setSpeed(speed):
    pwm.ChangeDutyCycle(speed)
