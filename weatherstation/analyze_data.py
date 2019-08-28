################################################################################
# Berkeley Atmos Club (ASAB) Weather Station Code
# 
# Read all the data from the data, make plots, etc.
################################################################################

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
time = data[:, 0]
temp = data[:, 1]
pres = data[:, 3]
humi = data[:, 4]

humi[np.where(humi == -999.0)] = np.nan

################################################################################
f, ax = plt.subplots(1, figsize=(8, 5))

ax.plot(temp, 'b')
ax.set_xlabel("Time")
ax.set_ylabel("Temperature ($^\\circ$C)")
ax.set_ylim([0, 40])
plt.tight_layout()

fname = "temperature.png"
plt.savefig(fname, dpi=80)
print("Saved {}".format(fname))
plt.close()
################################################################################
f, ax = plt.subplots(1, figsize=(8, 5))

ax.plot(pres, 'r')
ax.set_xlabel("Time")
ax.set_ylabel("Pressure (hPa)")
ax.set_ylim([1025, 970])
plt.tight_layout()

fname = "pressure.png"
plt.savefig(fname, dpi=80)
print("Saved {}".format(fname))
plt.close()
################################################################################
f, ax = plt.subplots(1, figsize=(8, 5))

ax.plot(humi, 'm')
ax.set_xlabel("Time")
ax.set_ylabel("Humidity (%)")
ax.set_ylim([0, 100])
plt.tight_layout()

fname = "humidity.png"
plt.savefig(fname, dpi=80)
print("Saved {}".format(fname))
plt.close()
################################################################################
