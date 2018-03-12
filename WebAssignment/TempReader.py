#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys

def readTemp():
     tempfile = open("/sys/bus/w1/devices/28-00000696404d/w1_slave")
     tempfile_text = tempfile.read()
     currentTime=time.strftime('%x %X %Z')
     tempfile.close()
     tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
     tempF=tempC*9.0/5.0+32.0
     return [currentTime, tempC, tempF]
def logTemp():
     con = mydb.connect('/home/pi/Desktop/ELSpring2018/WebAssignment/tempChart.db')
     with con:
          try:
               [t,C,F]=readTemp()
               print "Temperature Read: %s F" %F
               cur = con.cursor()
               #sql = "insert into tempt values(?,?,?)"
               cur.execute('insert into tempt values(?,?,?)', (t,C,F))
               print "Temperature logged"
          except:
               print "Error!!"


print readTemp()
logTemp()
