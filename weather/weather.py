import requests
import json
import os
import win32com.client
import requests

city=input("Enter the name of the city\n")
#speaker = win32com.client.Dispatch("SAPI.SpVoice")
url=f"https://api.weatherapi.com/v1/current.json?key=2e33fd25c43948aeb60180137230904&q={city}&aqi=no"

r=requests.get(url)
# print(r.text)

wjosn=json.loads(r.text)
