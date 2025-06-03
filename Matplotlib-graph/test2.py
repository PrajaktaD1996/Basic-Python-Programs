from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu


class demo(FloatLayout):
    def drp(self):
        self.menu_list=[
                {
                    "viewclass":"OneLineListItem",
                    "text":"example-1",
                    "on_release":lambda x = "example-1":self.test1()
                },
                {
                     "viewclass":"OneLineListItem",
                    "text":"example-2",
                    "on_release":lambda x = "example-2":self.test2()

                 }
                ]
        self.menu = MDDropdownMenu(
                caller = self.ids.menu,
                items = self.menu_list)
        self.menu.open()

    def test1(self):
        print("test-1 is  pressed")
    def test2(self):
        print("test-2 is pressed")
         
    Builder.load_file("demo.kv")
    #pass

class Main(MDApp):
    def build(self):
        return demo()
Main().run()
