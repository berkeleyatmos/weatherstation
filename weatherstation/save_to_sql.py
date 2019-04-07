import numpy as np
import datetime as dt
import os
import time
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import pymysql


fname = "data.txt"
time_interval = 1
sql_hostname = 'mysql'
sql_username = 'hpeter'

with open("sql_password") as f:
    sql_password = f.read()

with open("ssh_password") as f:
    ssh_password = f.read()
sql_main_database = 'hpeter'
sql_port = 3306
ssh_host = 'ssh.ocf.berkeley.edu'
ssh_user = 'hpeter'
ssh_port = 22

while True:
    os.system("./read_sensors.py")
    
    output = np.loadtxt("current_measurements.txt")
    temperature1 = output[0]
    temperature2 = output[1]
    pressure = output[2]
    humidity = output[3]
    
    current_date = dt.datetime.now()
    date = current_date.strftime("%y%m%d%H%M%S")        

    #TODO: it might be bad to open ssh connection once every time_interval seconds
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                passwd=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port, autocommit=True)
        #Sample read query
        query = "SELECT temperature1 from weatherdata;"
        data = pd.read_sql_query(query, conn)
        
        #sample insert command
        insert_command = "INSERT INTO weatherdata VALUES({},{},{},{},{});".format(date, temperature1, \
                                    temperature2, pressure, humidity)
        cur = conn.cursor()
        cur.execute(insert_command)
        conn.close() 

    time.sleep(time_interval)
