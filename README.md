# Introduction

This site hosts the code used in a weather station created by the Atmospheric Science At Berkeley (ASAB) club. 
The station consists of a Raspberry Pi equipped with several sensors that must communicate with the server.

The following README will serve as an guide and notebook for the project. 

# Login

## With Wifi

On Airbears2 the station's IP address is 10.142.21.24. 
Add the following line to your `~/.ssh/config` so that you can SSH to the Pi with just `ssh weatherstation`:

```bash
Host weatherstation
	HostName 10.142.21.24
	User pi
```

For obvious reasons, we will not post the password.

## With Ethernet

See https://stackoverflow.com/questions/16040128/hook-up-raspberry-pi-via-ethernet-to-laptop-without-router maybe?

# Using This Repo

Go to the directory you wish to download this repo in, and type `git clone https://github.com/berkeleyatmos/weatherstation.`
The `weatherstation` folder contains libraries and scripts to gather data.
The `misc` folder is for miscellaneous files we need to add to each weatherstation during setup.

## Setting Up Your Pi

Here we will keep some notes for starting up a new pi (because presumably we will be doing this multiple times).
Right now I will just post a few notes of things that are not obvious---later it will be more structured.

1. For some reason, you have to do `sudo apt install libatlas-base-dev` for python3 numpy to work. Don't ask.
2. Put `misc/atmos_startup_commands.sh` in `etc/init.d/`  #!FIXME: this did nothing... 
3. ...

# To Do

- Fill out this README fully, especially the _Setting Up Your Pi_ section.

- Create script for automatic updates that save to a database. Ideas for now:

	- Use OCF's free MySQL access 
	
	- Hash the password

	- Modify `save_data.py` to upload data to MySQL

- Make a simple website for the station to visualize the data. 
