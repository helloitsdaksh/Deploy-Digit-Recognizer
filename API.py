from flask import Flask,jsonify,request
import base64
from tensorflow.keras.models import load_model
from cv2 import *
import numpy as np


app = Flask(__name__)

model = load_model("Deploy-Digit-Recognizer/ model.h5")
def convertImage(imgData1):
	with open('Deploy-Digit-Recognizer/images/output.jpg','wb') as output:
		output.write(base64.b64decode(imgData1["base64"]))

@app.route('/')
def index():
    return jsonify({"Inputs" : "base64code"})

@app.route('/predict/',methods=['GET','POST'])
def predict():
	print("debug")
	image_data = request.get_json()
	convertImage(image_data)
	image_path = "Deploy-Digit-Recognizer/images/output.jpg"
	img_array = cv2.imread(image_path)
	new_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
	new_array = np.invert(new_array)
	new_array = cv2.resize(new_array, (28,28))
	new_array = new_array.reshape(1,28,28,1)
	y_pred = np.argmax(model.predict(new_array), axis=-1)
	print(y_pred)
	y_pred= y_pred.tolist()	
	return jsonify({"result" : y_pred})

if __name__ == "__main__":
	app.run()
	