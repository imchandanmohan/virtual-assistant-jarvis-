# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:17:28 2020

@author: Chandan
"""

import wikipedia
import a

dict_num = {"one" : 1,
            "short": 1,
            "two" : 2,
            "three" : 3,
            "long": 3
    }

def fun_wikipedia(text):
    a.speak("searching Wikipedia...")
    a.eng1_rate(160)
    a.speak("sir document is long should i retrive as it is or shell i short it up")
    result = a.takecommand()
    result = result.split()
    result = result[0]
    result = int(dict_num[result])
    print(result)
    query = text.replace("wikipedia","")
    result = wikipedia.summary(query, sentences = result)
    a.speak(result)

    
            
    






