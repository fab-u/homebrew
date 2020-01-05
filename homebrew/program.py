import time
import step
import motor
import tempControl

steps = []

for i in range(5):
  steps.append(step.step(0,0,0))

currentStep = 0
currentTime = 0
startTime = 0

isRunning = False

def start():
  startTime = time.time()
  _initStep(steps[currentStep])

def update():
  currentTime = time.time() - startTime
  if(currentTime >= steps[currentStep].time):
    currentStep = currentStep + 1
    _initStep(steps[currentStep])

def _initStep(step):
    tempControl.setTemp(step.temp)
    motor.setSpeed(step.speed)

