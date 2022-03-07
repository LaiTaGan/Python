from turtle import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
#graph
import matplotlib.pyplot as plt
import csv
from tkinter import * 
from tkinter.filedialog import askopenfilename
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
Builder.load_file('baseframe.kv')


class ContentNavigationDrawer(BoxLayout, MDList):
    pass


class ContentNavBtm(Screen):
    pass
    # def __init__(self):
    #     self.load = Loadfile()
# class Loadfile(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.box = BoxLayout()
#     def on_load_csv(self):
#         Tk().withdraw()
#         filename = askopenfilename()

#         x = []
#         y = []
#         #read csv file
#         with open(filename,'r') as csvfile:
#             lines = csv.reader(csvfile, delimiter=',')
#             for row in lines:
#                 x.append(row[0])
#                 y.append(int(row[1]))
    
#         #graph background color
#         plt.figure(facecolor='black') 
#         plt_color=plt.axes()
#         plt_color.set_facecolor((0.06,0.06,0.06)) 
#         #legends
#         plt.plot(x, y, color = 'g', linestyle = 'dashed',
#                 marker = 'o',label = "TH1")
#         #title
#         ax = plt.gca()
#         plt.title('Apollo Desktop', fontsize = 20)
#         ax.title.set_color('white')
#         #x-axis
#         plt.xlabel('Time(s)')
#         ax.xaxis.label.set_color('white')
#         ax.tick_params(axis='x', colors='white')
#         #y-axis for temp
#         plt.ylabel('Temperature(C)')
#         ax.yaxis.label.set_color('white')
#         ax.tick_params(axis='y', colors='white')
#         #y-axis for power
#         ax_power = ax.twinx()
#         plt.ylabel('Power(W)')
#         ax_power.yaxis.label.set_color('white')
#         ax_power.tick_params(axis='y', colors='white')
    
#         plt.grid()
#         ax.legend()

#         graph = self.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
#         return graph

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #self.theme_cls.primary_hue = "100"
        mainscreen = ScreenManager()
        mainscreen.add_widget(ContentNavBtm())
        return mainscreen
    
if __name__ == "__main__":
    app =MainApp()
    app.run()
