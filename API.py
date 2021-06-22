from flask import Flask,jsonify,request
from flask_restful import Api, Resource
import base64, re
import tensorflow as tf
import cv2
import sys
import numpy as np
from main import *
app = Flask(__name__)

model = tf.keras.models.load_model("Deploy-Digit-Recognizer/ model.h5")


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



if __name__ == "__main__":
    app.run(debug = True)
