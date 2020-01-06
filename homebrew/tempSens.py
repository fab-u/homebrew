import os, time
import gui

#sensor = '/sys/bus/w1/devices/28-031868c5fcff/w1_slave'  old sensor
sensor = '/sys/bus/w1/devices/28-03163386d7ff/w1_slave'

#Returns temperature values from sensor as float
def get() :
    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()

    pos = lines[1].find('t=')
    if pos != -1:
        temp_string = lines[1][pos+2:]
        temp_c = float(temp_string) / 1000.0

        gui.ui.lcd_showisttemp.display(temp_c)

        return temp_c
    else:
        return 0
