#!/usr/bin/env python3

################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# This is the main library for interacting with the sensors on
# the weather station.
################################################################################
import Adafruit_BME280 as BME280
import DHT22
import pigpio
import os
from time import sleep


### Setup

## BME280
# create sensor object
BME280_sensor = BME280.BME280(t_mode=BME280.BME280_OSAMPLE_8, p_mode=BME280.BME280_OSAMPLE_8, h_mode=BME280.BME280_OSAMPLE_8)

## DHT22: 
# instantiate a pi object
pi = pigpio.pi()
# intantiate a sensor object at 4th pin
DHT22_sensor = DHT22.sensor(pi, 4)
# trigger now to calibrate
DHT22_sensor.trigger()


### Functions for interacting with the sensors

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
