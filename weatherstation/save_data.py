#!/usr/bin/env python3

################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# Here we will take the data from 'read_sensor.py' and upload to MySQL
################################################################################

import os

cwd = os.getcwd()
os.system("{}/read_sensors.py".format(cwd))
