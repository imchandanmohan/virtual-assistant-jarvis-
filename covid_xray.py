# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:06:38 2020

@author: Chandan
"""
from engine import Engine
import engine as en
import os
import tensorflow as tf
import cv2
import os
import numpy as np
import time

model = tf.keras.models.load_model('covid19.model')

ass1 = Engine()

path_list =["C:\\Users\\Chandan\\Desktop\\","C:\\Users\\Chandan\\Downloads\\"]

def find(name, path):
    try:
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name), 1
            else:
                return None,0
    except Exception as e:
        ass1.speak("unable to find file sir")
        
def deep_network(path):
    try:
        ass1.speak("analysing....")
        print(path)
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (224, 224))
        ass1.engine_rate(150)
        ass1.speak("hmmmmhmmm hmmm")
        ass1.engine_rate(210)
        image = np.array(image) / 255.0
        image = image.reshape(1,224,224,3)
        pred = model.predict(image)
        predIdxs = np.argmax(pred, axis=1)
        return int(predIdxs)
    except Exception as e:
        ass1.speak("image is not in right formate")

def pred_speak(num):
    if 1 == num:
        ass1.speak("sir i am really happy to say you are corona negitive")
    if 0 == num:
        ass1.speak("sir sorry to say")
        ass1.engine_rate(160)
        ass1.engine_volume(0.6)
        #Waits 1 second
        time.sleep(1)
        ass1.speak("but you are corona positive to my analysis ")
        ass1.engine_rate(210)
        

def predict_xray():
    result = None
    flag = 0
    ass1.speak("what is the file name sir")
    command = en.wait_for_command()
    print(command)
    for path in path_list:
        file_name = command.lower()
        file_name = file_name+".jpeg"
        result,flag = find(file_name,path)
        try:
            if result != "None" and flag == 1:
                result = deep_network(result)
                pred_speak(result)
                break        
        except:
            ass1.speak("something as gone wrong with me please inform to my master")
        

        

        
        
