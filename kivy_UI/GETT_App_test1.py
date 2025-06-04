#:kivy 1.0

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.config import Config
from time import sleep
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import pandas as pd
from tabulate import tabulate

from datetime import datetime
import serial as ser
import time
import os
import signal
import logging
import serial
import numpy
from kivy.uix.button import Button
#import serial_read

#name = "/dev/ttyUSB"
#s_port = ser.Serial("/dev/ttyUSB0", 9600, timeout = 4)
#sleep_time_s =60
#product_group = "Electronic Under Test(EUT)"
#command1 = '<A,ABOUT>'            #VITAL_185
#command2 = '<A,SAMPLE>'           #VITAL_185
#baud_rate = 9600

#s_port.write(command1.encode())
#ser_about = s_port.readlines()   
#print(ser_about)
#s_port.write(command2.encode())
#ser_data = s_port.readlines()
#s_port.close()


Config.set('graphics','resizable','0')
Config.set('graphics','width','700')
Config.set('graphics','height','700')

pb = ProgressBar(max=1000)
pb.value = 750

class FirstWindow(Screen):
    steps = 6
    def press_it(self):
        name = "/dev/ttyUSB"
        s_port = ser.Serial("/dev/ttyUSB0", 9600, timeout = 4)
        sleep_time_s =60
        product_group = "Electronic Under Test(EUT)"
        command1 = '<A,ABOUT>'            #VITAL_185
        command2 = '<A,SAMPLE>'           #VITAL_185
        command3 = '<A,HEADER>'
        baud_rate = 9600

        s_port.write(command1.encode())
        ser_about = s_port.readlines()
        #print(ser_about)
        s_port.write(command2.encode())
        ser_data = s_port.readlines()
        x=str(ser_data).split('\\t')
        #print(x)
        #df = pd.DataFrame(x)
        #print(df)
        s_port.write(command3.encode())
        ser_data_abt = s_port.readlines()
        y=str(ser_data_abt).split('\\t')
        
        #re = dict(map(lambda i,j:(i,j),y,x))
        #print(re)

        df = pd.DataFrame(list(zip(y,x)),columns=['Packet_Datail','Value'])
        #print(df)
        
        layout = GridLayout(cols = 1,padding = 0)
        #layout = FloatLayout()
        popupLabel = Label(text = "About Device: "+ str(ser_about),pos=(1,1),font_size=13,size_hint=(0.0,0.2),halign="left",valign="top") ##Dummy Vital device connected
        abtLabel = Label(text="Device Packet:\n" +str(df),pos=(1,1),font_size=13,size_hint=(0.0,5.2),halign="left",valign="top")    ###multiple lables can be added 
        #dataLabel = Label(text="Packet Detail: "+str(y))
        
        closeButton = Button(text = "Click to Proceed") #Exit
        layout.add_widget(popupLabel)
        layout.add_widget(abtLabel)
        #layout.add_widget(dataLabel)
        layout.add_widget(closeButton)

        popup= Popup(title = 'Device Info:',content = layout)
        popup.open()
        closeButton.bind(on_press = popup.dismiss)
        sleep(2)

    def on_release(self):
        current = self.ids.my_progress_bar.value
        if current == 1:
            current =0
        current +=0.10
        self.ids.my_progress_bar.value = current


        
        
class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass


class ForthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

#Designate to load .kv design file 
kv = Builder.load_file('new_window.kv')

class GETTApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    
    GETTApp().run()






