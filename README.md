# Deploy-Digit-Recognizer

##Steps to run the Module on local host
- `pip install requirements.txt`
- run the app.py by using `python app.py`
- copy the link http://127.0.0.1:5000/ on to postman
- `/` is the index page which uses `GET` method 
- `/predict/` is the fucntion which predicts the output and which uses `POST` method 
  * keep the input in the `POST` method as the following:
    1. RAW and JSON as the input
    2. {
          "base64" : "base64 encoded image String"
       }
## This Module is also deployed on to heroku 
- follow the link : https://digit-recoginition.herokuapp.com/
