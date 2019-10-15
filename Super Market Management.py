from flask import Flask
app = Flask(__name__)                                
@app.route('/')                                       
def Welcome():        
    return '<h1>Deployed</h1>'
    
