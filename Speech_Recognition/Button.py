# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:18:15 2020

@author: Admin
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.dropdown import DropDown


class VgxMainScreen(Widget):
    pass

class VgxUI(Widget):
    pass


class VgxApp(App):
    def build(self):
        return VgxUI()

if __name__ == '__main__':
    VgxApp().run()