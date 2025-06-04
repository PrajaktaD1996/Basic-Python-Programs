#Basic Hantek animation

import matplotlib.pyplot as plt
import numpy as np
import pylab
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,

pylab.title('Scope Visualisation Example')

ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
#pylab.title('Scope Visualisation Example')
# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

pylab.show()
