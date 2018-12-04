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

with open("data.txt", "a") as f:
	while True:
	
		os.system("./read_sensors.py")
		
		output = np.loadtxt("current_measurements.txt")
		temperature = output[0]
		pressure = output[1]
		humidity = output[2]
		
		current_date = dt.datetime.now()
		#date = current_date.strftime("%Y/%m/%d %H:%m:%S")
		date = current_date.strftime("%H%m%S")
		
		#print("{} | {} °C | {} hPa | {} % RH".format(date, temperature, pressure, humidity))
	
		f.write("{} {} {} {}\n".format(date, temperature, pressure, humidity))
	
		time.sleep(5)
