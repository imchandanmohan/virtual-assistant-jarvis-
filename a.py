# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:30:03 2020

@author: Chandan
"""
import pyttsx3
import speech_recognition as sr


engine1 = pyttsx3.init()

MASTER = "Sir"

#speech speed
def eng1_rate(value):
    rate = engine1.getProperty('rate')
    engine1.setProperty('rate', value)

#speech volume
volume = engine1.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                       #printing current volume level
engine1.setProperty('volume',1.0)

#assisstent
voices = engine1.getProperty('voices')
engine1.setProperty('voices', voices[1].id)

def speak(text):
    engine1.say(text)
    engine1.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    with open("microphone-results1.wav", "wb") as f:
        f.write(audio.get_wav_data())
    
    
    try:
        print('Recognizing...')
        #query = r.recognize_google(audio, language = 'en-IN',show_all=True)
        query = r.recognize_google(audio, language = 'en-IN')
        print(query)
        return query
    
    except Exception as e:
        print("pardon please say again")
        return None