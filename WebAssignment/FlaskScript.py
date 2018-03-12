from flask import Flask, render_template, request
from datetime import datetime
import sqlite3
 
app = Flask(__name__)
@app.route('/')
def htmlLoader():
     return render_template('TempWebServer.html')
 
@app.route('/',methods=['POST'])
def Data():
     if request.method=='POST':
         startDate=request.form['startDate']
         endDate=request.form['endDate']
         tempStartDate = datetime.strptime(startDate,'%Y-%m-%d')
         tempEndDate = datetime.strptime(endDate,'%Y-%m-%d')
         startDateKey = tempStartDate.strftime('%m/%d/%Y')
         endDateKey = tempEndDate.strftime('%m/%d/%Y')
         conn = sqlite3.connect('/home/pi/ELSpring2018/WebAssignment/tempChart.db')
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM tempt WHERE date BETWEEN ? AND ?', (startDateKey, endDateKey,))
       
     return render_template('TempWebServer.html', data=cursor.fetchall(),startDate=startDate, endDate=endDate)
	 
if __name__ == "__main__":
     app.run(host='0.0.0.0', port=80, debug=True)