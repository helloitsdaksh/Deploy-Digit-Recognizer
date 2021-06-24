from flask import Flask,jsonify,request
import base64
from tensorflow.keras.models import load_model
from main import *


app = Flask(__name__)

model = load_model("model.h5")
def convertImage(imgData1):
    print(imgData1)
    with open("output.jpg",'wb') as output:
        output.write(base64.b64decode(imgData1["base64"]))
        

@app.route('/')
def index():
    return jsonify({"Inputs" : "base64code"})

@app.route('/predict/',methods=['POST'])
def predict():
    print("debug")
    image_data = request.get_json()
    print(f"debugging the api{image_data}")
    convertImage(image_data)
    
    return jsonify({"result" : init()})

if __name__ == "__main__":
	app.run()
	