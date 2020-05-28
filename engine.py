# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:23:42 2020

@author: Chandan
"""
import pyttsx3
import speech_recognition as sr


class Engine:
    
    def __init__(self):
        self.name = pyttsx3.init()   

    def engine_rate(self,value):
        rate = self.name.getProperty('rate')
        self.name.setProperty('rate', value) #210
        
    def engine_volume(self,value):
        volume = self.name.getProperty('volume')                      
        self.name.setProperty('volume',value) #1.0        
                 
    def speak(self,text):
        self.name.say(text)
        self.name.runAndWait()

def wait_for_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            r.dynamic_energy_threshold = True
            audio = r.listen(source)
        
        with open("chandan.wav", "wb") as f:
            f.write(audio.get_wav_data())
        
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language = 'en-IN')
            return query
        
        except Exception as e:
            print(e)
            return None