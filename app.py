from flask import Flask,render_template,url_for
from sqlalchemy import create_engine,text
import os

app = Flask(__name__)
db_connection_string=os.environ['alchym']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
})

    
with engine.connect() as conn:
    rows = conn.execute(text("SELECT tesla3numbers.indicators, tesla3numbers.Numbers, teslasnumbers.Numbers, teslaynumbers.Numbers FROM tesla3numbers left JOIN teslasnumbers ON tesla3numbers.indicators = teslasnumbers.indicators left JOIN teslaynumbers ON tesla3numbers.indicators = teslaynumbers.indicators;"))
  
#print(rows[0])


@app.route('/')
def index():
	return render_template('index.html', rows=rows)

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)