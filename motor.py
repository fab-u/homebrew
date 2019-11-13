import RPi.GPIO as GPIO
class motor:
    def __init__(self, frequencie):
        self.frequencie = frequencie
        self.dutyCycle = dutyCycle
        GPIO.setup(13, GPIO.OUT)
        self.pwm = GPIO.PWM(13,frequencie)

    def start(speed):
        pwm.start(speed)
        
    def stop():
        pwm.stop()

    def setSpeed(speed):
        pwm.ChangeDutyCycle(speed)
