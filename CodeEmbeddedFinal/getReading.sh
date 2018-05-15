#!/bin/sh
echo $(date) >> bash_cron_log.txt
/usr/bin/python /home/pi/CodeEmbeddedFinal/sheetReader.py 
