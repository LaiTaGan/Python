from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from Tabs.MainTab import MainTab
from Tabs.RecipeTab import RecipeTab
from Tabs.GraphTab import GraphTab
from Tabs.TestScriptTab import TestScriptTab

Builder.load_file('Containers/MainContainer.kv')

class MainContainer(TabbedPanel):
    pass