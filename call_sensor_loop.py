#!/usr/bin/env python3

import pigpio
import DHT22
import os
from time import sleep

# instantiate a pi object
pi = pigpio.pi()

# intantiate a sensor object at 4th pin
s = DHT22.sensor(pi, 4)

# trigger now to calibrate
s.trigger()

# trigger the sensor every few seconds
dt = 5 
while True:
    sleep(1)
    s.trigger()
    hum = s.humidity()
    temp = s.temperature()
    print("RH: {:3.1f} % T: {:3.1f} C".format(hum, temp))
    
