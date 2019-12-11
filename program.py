import time
import step
import motor
import tempControll

steps = []
currentStep = 0
currentTime = 0
startTime = 0

def start():
  startTime = time.time()
  _initStep(steps[currentStep])

def update():
  currentTime = time.time() - startTime
  if(currentTime >= steps[currentStep].time):
    currentStep = currentStep + 1
    _initStep(steps[currentStep])

def _initStep(step):
    tempControll.setTemp(step.temp)
    motor.setSpeed(step.speed)

