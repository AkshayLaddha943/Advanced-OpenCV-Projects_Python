# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 00:57:34 2020

@author: Admin
"""

import operator
import speech_recognition as sr
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

r = sr.Recognizer() 
mic = sr.Microphone()
                          
def get_operator_fn(op):
    return {
        'plus' : operator.add,
        '-' : operator.sub,
        'multiply' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


class MyGrid(Screen):
    pass


class SecondWindow(Screen):
    def microphone(self):
        
        with mic as source:
            r.adjust_for_ambient_noise(source)    
            self.audio = r.listen(source)
        self.text = r.recognize_google(self.audio)
     
    def result(self):
        self.r = self.text
        return eval(self.r)
        
        

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("D:\\Speech_Recognition\\my.kv")

class MyApp(App):
    def build(self):
        return kv
    

if __name__ == '__main__':
    MyApp().run()