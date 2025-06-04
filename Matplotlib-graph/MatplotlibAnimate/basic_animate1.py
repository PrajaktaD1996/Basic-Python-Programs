##################Date: 17-4-24
#####ploting graph in two different windows


import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

x1 = np.arange(0, 2*np.pi, 0.01)
x2 = np.arange(0,2*np.pi,0.01)
line1, = ax1.plot(x1, np.sin(x1))
line2, = ax2.plot(x2,np.cos(x2))


def animate(i):
    line1.set_ydata(np.sin(x1 + i / 50))  # update the data.
    line2.set_ydata(np.cos(x2 +i/50))
    return line1,line2


ani1 = animation.FuncAnimation(
    fig1, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
