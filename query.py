# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:19:21 2020

@author: Chandan
"""


    
ass_close = ["bye","close","take rest"]


ass_read = ["ok","wake","are you","ok jarvis"]


ass_confirm = ["leave","nothing","i can take care"]

    

def close(text):
    if text in ass_close:
        return True
    return False

def read(text):
    if text in ass_read:
        return True
    return False  

def confirm(text):
    if text in ass_confirm:
        return True
    return False

 
