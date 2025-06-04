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
from kivy.uix.button import Button
import serial_read

Config.set('graphics','resizable','0')
Config.set('graphics','width','700')
Config.set('graphics','height','700')

pb = ProgressBar(max=1000)
pb.value = 750

class FirstWindow(Screen):
    steps = 6
    def press_it(self):
        y0 = self.steps+1
        y = serial_read.funout()
        y2 = str(y)
        y3 = y2.split()
        print(y3)

        layout = GridLayout(cols = 1,padding = 10)
        popupLabel = Label(text = "Vital-185 Connected"+ "\nHello") ##Dummy Vital device connected
        anotherLabel = Label(text="text here" + "text here 2"+ str(y3)+str(y0))    ###multiple lables can be added 
        
        closeButton = Button(text = "Exit")
        layout.add_widget(popupLabel)
        layout.add_widget(anotherLabel)
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






