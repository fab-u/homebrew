import os, time
import gui

#sensor = '/sys/bus/w1/devices/28-031868c5fcff/w1_slave'  old sensor
sensor = '/sys/bus/w1/devices/28-03163386d7ff/w1_slave'

#Returns temperature values from sensor as float
def get() :
    try:
        f = open(sensor, 'r')
        lines = f.readlines()
        f.close()

        pos = lines[1].find('t=')
        if pos != -1:
            temp_string = lines[1][pos+2:]
            temp_c = float(temp_string) / 1000.0
            print(temp_c)

            #gui.ui.setIstTemp(temp_c)
            try:
                gui.ui.lcd_showisttemp.display(temp_c)
            except:
                print("temp display error")

            return temp_c
        else:
            return 0
    
    except:
        print("temp error")
