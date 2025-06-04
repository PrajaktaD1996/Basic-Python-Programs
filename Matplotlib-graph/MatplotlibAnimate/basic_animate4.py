##################Date: 17-4-24
#####ploting graph in two different windows
######important result having sub_plot in same window.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig = plt.figure(figsize = (8,4))
###plt.style.use(['science','notebook','grid']) ###not big issue for styles, can be checked afterwards
#fig.tight_layout(pad=100.0 ) ##didnt worked out

##adding space between two subplots
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.9, top=0.9, wspace=0.4,hspace=0.6)
#plt.legend(loc = 'upper right',fontsize = 10)


#txt_str1='\n'/join((r'$\sigma_a=%.4f$



###imp###
ax1 = fig.add_subplot(2,1,1)
ax1.text(0.8,0.80,'Amplitude:',transform = ax1.transAxes,bbox = dict(facecolor='white',edgecolor='black'))
ax1.text(0.8,0.65,'Frequency:',transform = ax1.transAxes)

ax2 = fig.add_subplot(2,1,2)
ax2.text(0.8,0.80,'Amplitude:',transform = ax2.transAxes)
ax2.text(0.8,0.65,'Frequency:',transform = ax2.transAxes)
################################################################always commented

x1 = np.arange(0, 2*np.pi, 0.01)
x2 = np.arange(0,2*np.pi,0.01)

line1, = ax1.plot(x1, np.sin(x1))
amp1 = np.sin(x1)
#print(amp1)
#f1 = 1/x1
#print(f1)

###txt_str1='\n'/join((r'$\sigma_a=%.4f$'%(np.std(amp1)),r'$\sigma_b=%.4f$'%(np.std(amp1)))



###imp###
#ax1 = fig.add_subplot(2,1,1)
#txt_str1='\n'/join((r'$\sigma_a=%.4f$'%(np.std(amp1)),r'$\sigma_b=%.4f$'%(np.std(amp1)))###chek for its syntax and placement

#ax1.text(0.8,0.80,txt_str1,transform = ax1.transAxes,bbox = dict(facecolor='white',edgecolor='black'))
#ax1.text(0.8,0.65,'Amplitude:',transform = ax1.transAxes)
#ax1.text(0.8,0.65,'Frequency:',transform = ax1.transAxes)

#ax2 = fig.add_subplot(2,1,2)
#ax2.text(0.8,0.80,'Amplitude:',transform = ax2.transAxes)
#ax2.text(0.8,0.65,'Frequency:',transform = ax2.transAxes)

ax1.set_title("Sender CH-1")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("Time(s)")
ax1.grid()

line2, = ax2.plot(x2,np.cos(x2),color='green')
amp2 = np.cos(x2)
ax2.set_title("Receiver CH-2")
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("Time(s)")
ax2.grid()

def animate(i):
    line1.set_ydata(np.sin(x1 + i/50))  # update the data.
    line2.set_ydata(np.cos(x2 + i/50))
    return line1,line2


ani1 = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)
#####plt.title("text()",size=20)
#plt.figure(figsize = (4,3))
plt.show()
