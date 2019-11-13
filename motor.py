import RPi.GPIO as GPIO
class motor:
    def __init__(self, frequencie):
        self.frequencie = frequencie
        GPIO.setup(13, GPIO.OUT)
        self.pwm = GPIO.PWM(13,frequencie)

    def start(self, speed):
        self.pwm.start(speed)
        
    def stop(self):
        self.pwm.stop()

    def setSpeed(self, speed):
        self.pwm.ChangeDutyCycle(speed)
