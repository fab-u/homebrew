import time
import step
import motor
import tempControl
import param

steps = []

for i in range(5):
  steps.append(step.step(0,0,0))

currentStep = 0
currentTime = 0
startTime = 0

isRunning = False

def start():
  global startTime
  startTime = time.time()
  _initStep(steps[currentStep])

def update():
  global currentStep
  currentTime = time.time() - startTime
  print(currentTime, steps[currentStep].time)
  if(currentTime >= steps[currentStep].time):
    if(currentStep > 4):
      param.isOn = False
      currentStep = False
    else:
      currentStep = currentStep + 1
      _initStep(steps[currentStep])

def _initStep(step):
  global startTime
  startTime = time.time()
  tempControl.tempSet = step.heat
  motor.setSpeed(step.speed)

