#!/usr/bin/env python3

import pigpio
import DHT22
import os
import csv
from time import sleep

# instantiate a pi object
pi = pigpio.pi()

# intantiate a sensor object at 4th pin
s = DHT22.sensor(pi, 4)

# trigger now to calibrate
s.trigger()

# trigger the sensor every few seconds
dt = 1 #note: when running data, dt will likely be 300 or something higher.

# temporary counter. Fix the while loop so it runs automatically in the future.
counter = 15

# open the output file
with open('humidity_temperature.csv', 'w') as data_file:
    data = csv.writer(data_file, delimiter = '\n')

    while counter > 0:
        sleep(dt)
        s.trigger()
        hum = s.humidity()
        temp = s.temperature()
        print(str(counter) + ' seconds remaining in the program.')
        counter -= 1
        data.writerow(["RH: {:3.1f} % T: {:3.1f} C".format(hum, temp)])
