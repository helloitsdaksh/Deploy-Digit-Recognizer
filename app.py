from flask import Flask,jsonify,request
import base64
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


app = Flask(__name__)

model = load_model("model.h5")
def convertImage(imgData1):
	with open('images/output.jpg','wb') as output:
		output.write(base64.b64decode(imgData1["base64"]))

@app.route('/')
def index():
    return jsonify({"Inputs" : "base64code"})

@app.route('/predict/',methods=['GET','POST'])
def predict():
    print("debug")
    image_data = request.get_json()
    convertImage(image_data)
    image_path = "images/output.jpg"
    image = Image.open(image_path)
    image = image.resize((28,28))
    image = image.convert(mode="L")
    print(image.mode)
    image_array = np.array(image)
    image_array= np.invert(image_array)
    print(image_array.shape) 
    image_array = image_array.reshape(1,28,28,1)
    y_pred = np.argmax(model.predict(image_array), axis=-1)
    y_pred =  y_pred.tolist()
    return jsonify({"result" : y_pred})

if __name__ == "__main__":
	app.run()
	