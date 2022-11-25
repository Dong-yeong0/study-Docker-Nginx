from flask import Flask 
from apis.test import test 

app = Flask(__name__) 

app.register_blueprint(test) 

if __name__ == '__main__': 
	app.run(host='0.0.0.0', port=5000)