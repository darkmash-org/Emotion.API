import requests
import base64


# for converting url to base64
def to_base64(str_):
	str_ = str_.encode("ascii")
	str_ = base64.b64encode(str_)
	return str_.decode("ascii")
  

def Get_Emotion(url):
	requests.get("https://emotionapi.darkmash.repl.co/service/{to_base64(url)}")
    
url = input("Url of img : ") # Getting the img url from user..
emotion = Get_Emotion(url) # Getting emotion using the API

print(f"Emotion : {emotion}")
