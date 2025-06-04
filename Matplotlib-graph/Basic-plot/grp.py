from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class MainApp(MDApp):
   def build(self):
      self.theme_cls.theme_style = "Dark"
      self.theme_cls.primary_palette="BlueGray"
		
MainApp().run()
