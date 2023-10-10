from flask import Flask,render_template,url_for
import os

app = Flask(__name__)

import mysql.connector
db_config =  { 
  "host": os.environ['host'], 
  "user": os.environ['user'], 
  "password": os.environ['password'], 
  "database": os.environ['database']
  }
    

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()#Create a cursor to execute SQL queries:

cursor.execute("SELECT tesla3numbers.indicators, tesla3numbers.Numbers, teslasnumbers.Numbers, teslaynumbers.Numbers FROM tesla3numbers left JOIN teslasnumbers ON tesla3numbers.indicators = teslasnumbers.indicators left JOIN teslaynumbers ON tesla3numbers.indicators = teslaynumbers.indicators;")

rows = cursor.fetchall()
print(rows[0])

cursor.close()
conn.close()

@app.route('/')
def index():
	return render_template('index.html', rows=rows)

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)