import matplotlib.pyplot as plt
import csv
from tkinter import * 
from tkinter.filedialog import askopenfilename
#choose csv file from explorer
Tk().withdraw()
filename = askopenfilename()
x = []
y = []
#read csv file
with open(filename,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))

#graph background color
plt.figure(facecolor='black') 
plt_color=plt.axes()
plt_color.set_facecolor((0.06,0.06,0.06)) 
#legends
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "TH1")
#title
ax = plt.gca()
plt.title('Apollo Desktop', fontsize = 20)
ax.title.set_color('white')
#x-axis
plt.xlabel('Time(s)')
ax.xaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
#y-axis for temp
plt.ylabel('Temperature(°C)')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='y', colors='white')
#y-axis for power
ax_power = ax.twinx()
plt.ylabel('Power(W)')
ax_power.yaxis.label.set_color('white')
ax_power.tick_params(axis='y', colors='white')

plt.grid()
ax.legend()
plt.show()