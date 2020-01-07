import time
import datetime
import motor
import tempControl

class step:
  def __init__(self, time, temp, speed):
    self.speed = speed
    self.time = datetime.time(0,0,0)
    self.temp = temp
    