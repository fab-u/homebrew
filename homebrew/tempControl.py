import RPi.GPIO as GPIO

tempSet = 0 #Set Temperature in °C
hysteresis = 1 #hysteresis in °C

_isOn = False

gpio = 22 #Raspi GPIO pin 
def init():
    GPIO.setup(gpio, GPIO.OUT)

#Set Temperature 
def setTemp(temp):
    tempSet = temp
    print("temp set", temp)

#Update heat plate with current temperature values
def update(tempActual):
    try:
        if(tempActual < (tempSet - hysteresis)):
            GPIO.output(gpio, GPIO.HIGH)
            print("heat", tempSet, tempActual)
        elif(tempActual > (tempSet + hysteresis)):
            GPIO.output(gpio, GPIO.LOW)
            print("dont heat", tempSet, tempActual)
    except:
        print("heating error")

def off():
    GPIO.output(gpio, GPIO.LOW)
