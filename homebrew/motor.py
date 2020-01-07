import RPi.GPIO as GPIO

gpio = 18
frequencie = 200 

GPIO.setup(gpio, GPIO.OUT)
pwm = GPIO.PWM(gpio, frequencie)
pwm.start(0)

#Start with speed from 0 to 10
def start(speed):
    pwm.start(speed*10)

#Stop motor
def stop():
    pwm.stop()

#Speed from 0 to 10
def setSpeed(speed):
    pwm.ChangeDutyCycle(speed*10)
    print(speed)
