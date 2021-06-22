from flask import Flask,jsonify,request
from flask_restful import Api, Resource
import base64, re
import imageio
import tensorflow as tf

app = Flask(__name__)


def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
	#print(imgstr)
	with open('output.png','wb') as output:
		output.write(imgstr.decode('base64'))


@app.route('/')
def index():
    return jsonify({"Inputs" : "base64code"})

@app.route('/predict/',methods=['GET','POST'])
def predict():
	imgData = request.get_data()
	convertImage(imgData)
	print ("debug")
	# x = imread('output.png')
	return



if __name__ == "__main__":
    app.run(debug = True)
