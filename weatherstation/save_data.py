#!/usr/bin/env python3

################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# Here we will take the data from 'read_sensor.py' and upload to MySQL
################################################################################

import numpy as np
import datetime as dt


output = np.loadtxt("current_measurements.txt")
temperature = output[0]
pressure = output[1]
humidity = output[2]

current_date = dt.datetime.now()
date = current_date.strftime("%Y/%m/%d %H:%m:%S")

print("{} | {} °C | {} hPa | {} % RH".format(date, temperature, pressure, humidity))
