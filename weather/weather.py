import requests
import json
import os
import win32com.client
import requests

city=input("Enter the name of the city\n")
#speaker = win32com.client.Dispatch("SAPI.SpVoice")
url=f"https://api.weatherapi.com/v1/current.json?key="YOUR_API_KEY"={city}&aqi=no"

r=requests.get(url)
# print(r.text)

wjosn=json.loads(r.text)
