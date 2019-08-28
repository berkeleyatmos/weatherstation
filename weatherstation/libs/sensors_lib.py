################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# This is the main library: it contains functions that we can call in another 
# file to interact with the sensors on the Pi.
################################################################################
import libs.BME280_lib as BME280_lib
import libs.DHT22_lib as DHT22_lib
import pigpio
import os
from time import sleep


# Setup

## BME280
### create sensor object
BME280_sensor = BME280_lib.BME280(t_mode=BME280_lib.BME280_OSAMPLE_8, 
    p_mode=BME280_lib.BME280_OSAMPLE_8, h_mode=BME280_lib.BME280_OSAMPLE_8)

# DHT22: 
## instantiate a pi object
pi = pigpio.pi()
## intantiate a sensor object at 4th pin
DHT22_sensor = DHT22_lib.sensor(pi, 4)
## trigger now to calibrate
DHT22_sensor.trigger()


# Functions for interacting with the sensors

def BME280_read():
    """
    Call this function to get T, p from the BME280 sensor
    """
    # read sensor
    temp = BME280_sensor.read_temperature()
    pres = BME280_sensor.read_pressure()
    # hum = BME280_sensor.read_humidity() 

    # hPa
    pres /= 100

    return temp, pres


def DHT22_read():
    """
    Call this function to get T, RH from the DHT22 sensor
    """
    # trigger sensor
    DHT22_sensor.trigger()
    # read sensor
    hum = DHT22_sensor.humidity()
    temp = DHT22_sensor.temperature()

    return temp, hum
