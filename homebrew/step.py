import time
import motor
import tempControl

class step:
  def __init__(self, time, heat, speed):
    self.speed = speed
    self.time = time
    self.heat = heat
    