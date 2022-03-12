from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
from Screens.loginscreen import *


Builder.load_file('baseframe.kv')
Builder.load_file('Kivy_resources/widget_library.kv')

class ContentNavBtm(Screen):
    loginscreen= LoginScreen()

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_cyan = "400"
        mainscreen = ScreenManager()
        mainscreen.add_widget(ContentNavBtm())
        return mainscreen
    
if __name__ == "__main__":
    app =MainApp()
    app.run()
