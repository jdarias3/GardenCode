#!/usr/bin/env python

import sqlite3
from cgi import escape, parse_qs
import serial
import time

def application(environ, start_response):

     connection = None
     my_responsev = ""
     params = parse_qs(environ['QUERY_STRING'])
     humedad = escape(params.get('humedad',[''])[0])

ser = serial.Serial('/dev/ttyACM0', 9600,timeout=1.0) #Initializing the Serial$
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
        my_query = 'INSERT INTO humedad (id,humedad,datetime) VALUES(NULL,%s,CURRENT_TIMESTAMP);' %(msg,)

        try:
                connection = sqlite3.connect('/var/www/database/humedad.db' ,i$
                cursor = connection.cursor()
                print("TEST1")
                cursor.execute(my_query)
                print("TEST2")
                query_results = cursor.fetchone()
                my_response = 'Inserted %s at datetime' %(msg)
        except sqlite3.Error, e:
                my_response = "There is an error %s:" % (e)
        finally:
                connection.close()

        #status = '200 OK'
        #response_headers = [('Content-Type', 'text/plain'), 'Content-Length',$
        #start_response(status, response_headers)
        #return [my_response]
