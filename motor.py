import RPi.GPIO as GPIO

gpio = 12
frequencie = 2000 

pwm = GPIO.PWM(gpio, frequencie)

def start(speed):
    pwm.start(speed)
    
def stop():
    pwm.stop()

#Speed from 0 to 10
def setSpeed(speed):
    pwm.ChangeDutyCycle(speed*10)
