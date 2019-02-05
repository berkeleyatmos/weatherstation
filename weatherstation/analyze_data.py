#!/usr/bin/env python3

################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# Read all the data from the MySQL database, make plots, etc.
################################################################################

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
time = data[:, 0]
temp = data[:, 1]
pres = data[:, 3]
humi = data[:, 4]
#pres = data[:, 2]
#humi = data[:, 3]

humi[np.where(humi == -999.0)] = np.nan

f, ax = plt.subplots(1, figsize=(8, 5))
ax.plot(temp, 'b')
plt.savefig("temp.png")
plt.close()

f, ax = plt.subplots(1, figsize=(8, 5))
ax.plot(pres, 'r')
plt.savefig("pres.png")
plt.close()

f, ax = plt.subplots(1, figsize=(8, 5))
ax.plot(humi, 'm')
plt.savefig("humi.png")
plt.close()
