"""
Emotion API

By ~ Darkmash
"""

from deepface import DeepFace
from flask import Flask
import datetime
import requests
import random
import logging
import base64
import cv2
import os

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def main_func_():
  print("PING__UPTIME")  
  return """
  ######## DARKMASH ~ EMOTION API ~ V.1.0.0 #########<br>
  To use the service ,<br>
      /service/img_url_encoded_with_base64
  ####################################################
  """


@app.route('/service/<file_url>')
def main_func(file_url):

    try:
      base64_bytes = file_url.encode("ascii")
    
      sample_string_bytes = base64.b64decode(base64_bytes)
      file_url = sample_string_bytes.decode("ascii")
      
      response = requests.get(file_url)
  
  
      if response.status_code:
        in_t = f"{random.randint(90000000,90000000000000)}.{file_url.split('.')[-1]}"
        fp = open(in_t, 'wb')
        fp.write(response.content)
        fp.close()
      else:
        return "Some error regarding the link happend.. (somethin like the site was down)"
        
      img = cv2.imread(in_t)
      os.remove(in_t)
      
      result = DeepFace.analyze(img, actions=['emotion'])
    
      return result
      
    except:
      return "Some error occured.. (maybe something related to the link)"
  

app.run(host="0.0.0.0", port=8080)
