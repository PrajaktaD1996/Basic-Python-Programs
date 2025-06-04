##################Date: 18-4-24
#####ploting graph in two different windows
######important result having sub_plot in same window.

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import datetime
import matplotlib.dates as mdates
import pandas as pd

fig = plt.figure(figsize = (8,4))
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.9, top=0.9, wspace=0.4,hspace=0.6)
##channel-1
x1 = np.arange(0, 2*np.pi, 0.01)
###generated dummy frequency value by taking max and its invetred and *1000
#freq1_ver="{:.3f}".format(max(x1))
freq1_ver=(1/max(x1))*1000
freq1_ver="{:.3f}".format(freq1_ver)
freq1_str= str(freq1_ver)
ax1 = fig.add_subplot(2,1,1)
amp1 = np.sin(x1)
amp1_ver="{:.2f}".format(max(amp1))
amp1_str = str(amp1_ver)
###real time date to matplotlib
###########ax1.text(0.75,0.90,'Date:'+current_time,transform=ax1.transAxes)
ax1.text(0.75,0.80,'Amplitude:'+amp1_str+'V',transform=ax1.transAxes)
ax1.text(0.75,0.65,'Frequency:'+freq1_str+'Hz',transform = ax1.transAxes)
line1, = ax1.plot(x1, np.sin(x1))
ax1.set_title("Sender(CH-1)")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("Time(s)")
ax1.grid()

##channel-2
x2 = np.arange(0,2*np.pi,0.01)
freq2_ver=(1/max(x2))*1000
freq2_ver="{:.3f}".format(freq2_ver)
freq2_str=str(freq2_ver)
ax2 = fig.add_subplot(2,1,2)
amp2 = np.cos(x2)
amp2_ver = "{:.2f}".format(max(amp2))
amp2_str = str(amp2_ver)
ax2.text(0.75,0.80,'Amplitude:'+amp2_str+'V',transform = ax2.transAxes)
ax2.text(0.75,0.65,'Frequency:'+freq2_str+'Hz',transform = ax2.transAxes)
line2, = ax2.plot(x2,np.cos(x2),color='green')
ax2.set_title("Receiver(CH-2)")
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("Time(s)")
ax2.grid()

def animate(i):
    line1.set_ydata(np.sin(x1 + i/50))  # update the data.
    line2.set_ydata(np.cos(x2 + i/50))
    return line1,line2


ani1 = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.show()
