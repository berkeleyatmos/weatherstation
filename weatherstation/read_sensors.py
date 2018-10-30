#!/usr/bin/env python2

################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# In this file we import the functions from the `libs.sensors_lib` and use 
# them to read the sensors on the Pi. We then process the data.
################################################################################

import libs
from libs.sensors_lib import BME280_read, DHT22_read

### Read the sensors
temperature1, pressure = BME280_read()
temperature2, humidity = DHT22_read()

# Print values
print("From BME280: {} K, {} hPa".format(temperature1, pressure))
print("From DHT22:  {} K, {}% RH".format(temperature2, humidity))
