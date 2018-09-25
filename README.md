# Introduction

This site hosts the code used in a weatherstation created by the Atmospheric Science At Berkeley (ASAB) club. 
The station consists of a Raspberry Pi equiped with several sensors that must communicate with the server.

The following README will serve as an introductory guide on how to use the station and the code in this repository.

# Setup

On Airbears2 the station's ip address is 10.142.93.19. 
Add the following line to your `~/.ssh/config` so that you can ssh to the Pi with just `ssh weatherstation`:

```
Host weatherstation
	HostName 10.142.93.19
	User pi
```

For obvious reasons, I will not post the password.

# Using the Code

Section under construction.

# To Do

- Clean up code. Plan: either make a WeatherStation class or define useful functionss in one file. Import this file to use the functions or class so that interaction with sensors is clean and simple.

- Create script for automatic updates that save to a database. Perhaps use OCF's free MySQL access for this.

- Make a simple website for the station to visualize the data. 

- Finish this README...
