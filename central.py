#!/usr/bin/env python

import mysql.connector
from mysql.connector import Error
from cgi import escape, parse_qs
import serial
import time



#ser = serial.Serial('/dev/ttyACM0', 9600,timeout=1.0) #Initializing the Serial$ Linux
ser = serial.Serial('COM3', 9600,timeout=1.0)
ackArduino = '0'


while True:

        ACKvalue = input("Please enter the ACK code: ")
        ackArduino = str(ACKvalue)
        print("The ACK code is " + str(ACKvalue))

        ser.write(ackArduino)
     #print "Informacion de Arduino pedida \n"
        #time.sleep(30) # Delay in seconds
        msg = ser.readline()
     #print "MSg from Arduino"
        print (msg)
        

	 
		# Connect to MySQL database """
	try:
		conn = mysql.connector.connect(user='admin', password='root', host='192.168.0.11', database='Garden')
		if conn.is_connected():
			print('Connected to MySQL database')
			cursor = conn.cursor()
			cursor.execute("""INSERT INTO GardenMonitor(planta, humedad, temperatura,bomba) VALUES(%s,%s,%s,%s) """,["stevia",msg,38,1])
			conn.commit()
			
 
	except Error as e:
		print(e)
 
	finally:
		cursor.close()
		conn.close()
	 
