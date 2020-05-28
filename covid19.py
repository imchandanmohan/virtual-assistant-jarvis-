# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:40:40 2020

@author: Chandan
"""


import pyttsx3
import speech_recognition as sr
import requests
import json
import urllib
from engine import Engine

ass1 = Engine()



MASTER = "Sir"

url = 'https://api.covid19api.com/summary'
response = urllib.request.urlopen(url)



def speak_country(country_name,text):
    ass1.speak(MASTER+"new conformed cases in"+country_name+"are")
    ass1.engine_rate(150)
    #print(".......")
    #print(text)
    ass1.speak(text)
    ass1.runAndWait()

    

    
def new_covid_cases(country_name):
    json_data = json.loads(response.read())
    list_countries = json_data["Countries"]
    for i in list_countries:
        if i["Country"].lower() == country_name:
            result = i["NewConfirmed"]
            #print(resut)
            
    return str(result)





#can you confirm new covid-19 cases in {country}
def covid_19(query):
    ass1.speak("searching..."+MASTER)
    words = query.split()
    country_name = words[-1]
    result = new_covid_cases(country_name)
    speak_country(country_name,result)
    
    
    
