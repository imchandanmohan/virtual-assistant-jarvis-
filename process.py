# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:17:28 2020

@author: Chandan
"""
import wiki
import covid19
import covid_xray
import Time


def take_jarvis_query(text):
    
    if "wikipedia" in text.lower():
        wiki.fun_wikipedia(text.lower())
        
    elif "new covid-19 cases" in text.lower():
        covid19.covid_19(text.lower())
        pass
    elif "time" in  text.lower():
        Time.saytime()
        
    elif "predict my" in text.lower():
        covid_xray.predict_xray()
        
    else:
        return """sorry i am resticted to few operations and i 
                    think query was not one of that"""
    
            
    






