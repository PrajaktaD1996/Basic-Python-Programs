import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import time

goals = [0, 1, 2, 3, 4, 5, 6]

ax = plt.axes()
#ax.plot(seconds_since_epoch, goals)
ax.set_title('2018 FIFA World Cup Final')
ax.set_ylabel('Goals')
ax.set_xlabel('Time of Day (UTC)')
# Convert seconds-since-epoch numbers into struct_time objects and then to
# strings (you can use time.localtime() instead of time.gmtime() to get the
# time in your local timezone)
fmt = ticker.FuncFormatter(lambda x, pos: time.strftime('%H:%M', time.gmtime(x)))
ax.xaxis.set_major_formatter(fmt)

plt.show()
