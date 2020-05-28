import pyttsx3
import speech_recognition as sr
import datetime
from engine import Engine

ass = Engine()

def saytime():
	time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        ass.speak("good morning"+ MASTER)
        ass.runAndWait()
        
    elif time>=12 and time<18:
        ass.speak("good afternoon"+ MASTER)
        ass.runAndWait()
        
    else:
        ass.speak("good evening"+ MASTER)
        ass.runAndWait()