import time
import motor
import tempControl

class step:
  def __init__(self, time, temp, speed):
    self.speed = speed
    self.time = time
    self.temp = temp
    