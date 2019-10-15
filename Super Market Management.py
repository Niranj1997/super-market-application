from flask import Flask
import smtplib
app = Flask(__name__)                                
@app.route('/')                                       
def Welcome():        
    return '<h1>Deployed</h1>'
    
