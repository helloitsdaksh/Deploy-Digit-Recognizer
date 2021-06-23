from PIL import Image
import numpy as np
from keras.models import load_model
def init():
    model = load_model("model.h5")
    # print ("debug")
    image_path = "output.jpg"
    image = Image.open(image_path)
    image = image.resize((28,28))
    image = image.convert(mode="L")
    # print(image.mode)
    image_array = np.array(image)
    image_array= np.invert(image_array)
    # print(image_array.shape) 
    image_array = image_array.reshape(1,28,28,1)
    y_pred = np.argmax(model.predict(image_array), axis=-1)
    # print(y_pred)
    return y_pred.tolist()
if __name__ == '__main__':
    init()