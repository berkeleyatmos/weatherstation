import numpy as np
import datetime as dt
import os
import time
import paramiko
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import pymysql


fname = "data.txt"
time_interval = 15
sql_hostname = 'mysql'
sql_username = 'ankurmahesh'

with open("sql_password") as f:
    sql_password = f.read().replace("\n", "")

with open("ssh_password") as f:
    ssh_password = f.read().replace("\n", "")

sql_main_database = 'ankurmahesh'
sql_port = 3306
ssh_host = 'ssh.ocf.berkeley.edu'
ssh_user = 'ankurmahesh'
ssh_port = 22

while True:
    os.system("python2 read_sensors.py")    # must use python2 due to older libraries
    
    output = np.loadtxt("current_measurements.txt")
    temperature1 = output[0]
    temperature2 = output[1]
    pressure = output[2]
    humidity = output[3]
    
    current_date = dt.datetime.now()
    date = current_date.strftime("%y-%m-%d %H:%M:%S")        

    #TODO: it might be bad to open ssh connection once every time_interval seconds
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                passwd=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port, autocommit=True)

        #sample insert command
        insert_command = "INSERT INTO weatherdata VALUES(\"{}\",{},{},{},{});".format(date, temperature1, \
                                    temperature2, pressure, humidity)
        cur = conn.cursor()
        cur.execute(insert_command)
        conn.close() 

    time.sleep(time_interval)

    print(insert_command)
