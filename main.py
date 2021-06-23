# import tensorflow as tf
# import cv2
# import numpy as np

# def init():
#     model = tf.keras.models.load_model("Deploy-Digit-Recognizer/ model.h5")
#     print ("debug")
#     image_path = "Deploy-Digit-Recognizer/images/output.jpg"
#     img_array = cv2.imread(image_path)
#     new_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
#     new_array = np.invert(new_array)
#     new_array = cv2.resize(new_array, (28,28))
#     new_array = new_array.reshape(1,28,28,1)
#     y_pred = np.argmax(model.predict(new_array), axis=-1)
#     print(y_pred)
#     return y_pred.tolist()