################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# Here we will take the data from 'read_sensors.py' and upload to MySQL
################################################################################

import numpy as np
import datetime as dt
import os
import time

fname = "data.txt"
time_interval = 2 #seems to work best at 2 or 3
with open(fname, "a") as f:
    prev_temp2 = -999
    prev_humidity = -999
    while True:
        os.system("python2 read_sensors.py")    # must use python2 because of older libraries
        
        output = np.loadtxt("current_measurements.txt")
        temperature1 = output[0]
        temperature2 = output[1]
        pressure = output[2]
        humidity = output[3]
        
        #Correct any erroneous readings
        if temperature2 == -999:
            temperature2 = prev_temp2
            humidity = prev_humidity
        else:
            prev_temp2 = temperature2
            prev_humidity = humidity
    
        current_date = dt.datetime.now()
        #date = current_date.strftime("%Y/%m/%d %H:%M:%S")
        date = current_date.strftime("%H%M%S")
        
        data_string = "{} {} {} {} {}".format(date, temperature1, temperature2, pressure, humidity)
        
        print("Writing `{}` to {}.".format(data_string, fname))
        f.write(data_string + "\n")
        
        time.sleep(time_interval)
