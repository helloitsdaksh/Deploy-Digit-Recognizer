from flask import Flask,jsonify,request
import base64
from main import *
app = Flask(__name__)

def convertImage(imgData1):
	with open('Deploy-Digit-Recognizer/images/output.jpg','wb') as output:
		output.write(base64.b64decode(imgData1["base64"]))

@app.route('/')
def index():
    return jsonify({"Inputs" : "base64code"})

@app.route('/predict/',methods=['GET','POST'])
def predict():
	imgData = request.get_json()
	convertImage(imgData)
	print ("debug")	
	
	return jsonify({"result" : init()})
