import RPi.GPIO as GPIO

tempSet = 0

gpio = 13
GPIO.setup(gpio, GPIO.OUT)

def setTemp(temp):
    tempSet = temp

def update(tempActual):
    if(tempActual>tempSet):
        GPIO.output(gpio, GPIO.HIGH)
    else:
        GPIO.output(gpio, GPIO.LOW)

def off():
    GPIO.output(gpio, GPIO.LOW)
