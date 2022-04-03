from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
from Screens.loginscreen import *
from Containers.MainContainer import MainContainer

Builder.load_file('OS.kv')
Builder.load_file('Resources/widget_library.kv')

class NavigationSwitcher(Screen):
    loginscreen= LoginScreen()



class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_cyan = "400"
        mainscreen = ScreenManager()
        mainscreen.add_widget(NavigationSwitcher())
        return mainscreen
    
if __name__ == "__main__":
    app =MainApp()
    app.run()
