# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:17:06 2020

@author: Chandan
"""


import engine as en
from engine import Engine, wait_for_command
import query
import process

ass = Engine()
ass.engine_rate(210)

def listen():
    
    command = en.wait_for_command()
    try:
        result = None
        if query.close(command.lower()):
            flag_close = False
            ass.speak("are you sure sir? like, its ok ill wait for your command")
            confirm = en.wait_for_command()
            if query.confirm(confirm.lower()):
                ass.speak("fine sir! please call me if you need any assisstent")
                result = "close"
            if "ok" == command.lower():
                ass.speak("i am always hear for you sir")
            return result
        elif query.read(command.lower()):
            flag_read = True
            ass.speak("for you sir... always")
            run_jarvis()
        else:
            return None
    except:
        return None
    
def run_jarvis():
    result = None
    query = wait_for_command()
    result = process.take_jarvis_query(query.lower())
    if result!=None:
        ass.speak(result)
    ass.speak("any thing else sir")
    query = en.wait_for_command()
    if "no" == query.lower():
        ass.speak("ok sir")
    if "yes" == query.lower():
        ass.speak("cammand me sir")
        run_jarvis()
    ass.engine_rate(210)
        
    
    
        
if __name__ == "__main__":
    ass.speak("Initializing jarvis...")
    while True:
        res = listen()
        if res == "close":
            break


