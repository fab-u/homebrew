import RPi.GPIO as GPIO

def test():
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, GPIO.HIGH)