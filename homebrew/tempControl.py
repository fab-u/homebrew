import RPi.GPIO as GPIO

tempSet = 0 #Set Temperature in °C
hysteresis = 1 # hysteresis in °C

gpio = 13 #Raspi GPIO pin 
GPIO.setup(gpio, GPIO.OUT)

#Set Temperature 
def setTemp(temp):
    tempSet = temp

#Update heat plate with current temperature values
def update(tempActual):
    if(tempActual> (tempSet + hysteresis)):
        GPIO.output(gpio, GPIO.HIGH)
    elif(tempActual> (tempSet - hysteresis)):
        GPIO.output(gpio, GPIO.LOW)

def off():
    GPIO.output(gpio, GPIO.LOW)
