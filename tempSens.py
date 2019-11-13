import os, time

sensor = '/sys/bus/w1/devices/28-031868c5fcff/w1_slave'

def get() :
    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

