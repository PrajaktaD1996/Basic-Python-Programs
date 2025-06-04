import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-4, 4))
line, = ax.plot([], [], lw=3)
ax.set_title('txt')
ax.set_xlabel('date')
ax.set_ylabel('random')
# initialization function
def init():
    line.set_data([], [])
    return line,

# animation function.  
def animate(i):
    x = np.linspace(0, 3, 1050)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,
 
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=220, interval=20, blit=True)


plt.show()

#anim.save('Basic sine wave.mp4', writer = 'ffmpeg',fps=30)

