# Introduction

This site hosts the code used in a weather station created by the Atmospheric Science At Berkeley (ASAB) club. 
The station consists of a Raspberry Pi equipped with several sensors that must communicate with the server.

The following README will serve as an guide and notebook for the project. 

# Login

## With Wifi

As of now, the station's IP address seems to change every few reboots on Airbears2.
On the Pi, run `ifconfig` and look for the `inet` line under `wlan0` to get the IP.
Then run `ssh pi@<ip_address>` on your own machine and you should be in (with the proper password).

## With Ethernet

See https://stackoverflow.com/questions/16040128/hook-up-raspberry-pi-via-ethernet-to-laptop-without-router maybe?

# Using This Repo

Go to the directory you wish to download this repo in, and type `git clone https://github.com/berkeleyatmos/weatherstation.`
The `weatherstation` folder contains libraries and scripts to gather data.
The `misc` folder is for miscellaneous files we need to add to each weatherstation during setup.
The `docs` folder contains useful documentation on how to set up the station.

## Setting Up Your Pi

Here we will keep some notes for starting up a new pi (because presumably we will be doing this multiple times).
Right now I will just post a few notes of things that are not obvious---later it will be more structured.

1. For some reason, you have to do `sudo apt install libatlas-base-dev` for python3 numpy to work. Don't ask.
2. Run `sudo systemctl enable pigpiod` so that the PiGPIO daemon starts on start-up.
3. ...

# To Do

- Fill out this README fully, especially the _Setting Up Your Pi_ section.
