import RPi.GPIO as GPIO

gpio = 16
frequencie = 200 

GPIO.setup(gpio, GPIO.OUT)
pwm = GPIO.PWM(gpio, frequencie)

#Start with speed from 0 to 10
def start(speed):
    pwm.start(speed*10)

#Stop motor
def stop():
    pwm.stop()

#Speed from 0 to 10
def setSpeed(speed):
    pwm.ChangeDutyCycle(speed*10)
