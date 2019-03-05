#!/usr/bin/env python3

################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# Here we will take the data from 'read_sensor.py' and upload to MySQL
################################################################################

import numpy as np
import datetime as dt
import os
import time

fname = "data.txt"
time_interval = 1
with open(fname, "a") as f:
    while True:
        os.system("./read_sensors.py")
        
        output = np.loadtxt("current_measurements.txt")
        temperature1 = output[0]
        temperature2 = output[1]
        pressure = output[2]
        humidity = output[3]
        
        current_date = dt.datetime.now()
        #date = current_date.strftime("%Y/%m/%d %H:%M:%S")
        date = current_date.strftime("%H%M%S")
        
        data_string = "{} {} {} {} {}".format(date, temperature1, temperature2, pressure, humidity)
        
        print("Writing `{}` to {}.".format(data_string, fname))
        f.write(data_string + "\n")
        
        time.sleep(time_interval)
