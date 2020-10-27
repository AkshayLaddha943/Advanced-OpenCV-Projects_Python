# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:11:15 2020

@author: Admin
"""
import operator
import speech_recognition as sr
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen , FadeTransition

r = sr.Recognizer() 
mic = sr.Microphone()

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)


class MyGrid(Screen):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.add_widget(Label(text='Instructions :\n 1. Pronounce three digit number (like 142) as : One four two (for clarity)\n 2. Number 20 gives an error\n 3. After pressing the mic, wait for one second & then start speaking',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5}))
        
        self.btn = Button(text ="Next", 
                   font_size ="20sp", 
                   background_color =(1, 1, 1, 1), 
                   color =(1, 1, 1, 1), 
                   size =(32, 32), 
                   size_hint =(.2, .2), 
                   pos =(300, 250))
        self.btn.bind(on_press = SecondWindow.second())
        self.add_widget(self.btn)
        
        

    

class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)
        
    def second(self):
        layout = GridLayout(cols=2)
        self.lab = Label(text="Enter the calculation: ")
        self.ans = TextInput()
        
        layout.add_widget(self.lab, self.ans)



class MyApp(App):
    def build(self):
        sm = WindowManager(transition=FadeTransition())
        sm.add_widget(SecondWindow(name='FIRST'))
        sm.add_widget(MyGrid(name='SECOND'))
        return sm
    

if __name__ == '__main__':
    MyApp().run()