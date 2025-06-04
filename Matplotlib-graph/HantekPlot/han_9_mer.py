##getting real time hantek graph
###merging basic_animate_6.py and han_9.py 
###real-time han-data in format

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PyHT6022.LibUsbScope import Oscilloscope
import numpy as np
import pylab
import time 
import sys

def apply_data_smoothing(data, window=1):
    new_data = data[:window]
    for i, point in enumerate(data[window:-window]):
        new_data.append(sum(data[i-window:i+window+1])/(2*window+1))
    new_data.extend(data[-window:])
    return new_data


fig = plt.figure(figsize = (8,4))
plt.subplots_adjust(left=0.20, bottom=0.20, right=0.9, top=0.9, wspace=0.4,hspace=0.6)


sample_rate_index = 1
voltage_range = 0x01
cal_freq = 10
skip = 2 * 0x400
data_points = skip + 20 * 0x400

##ch-1
scope = Oscilloscope()
scope.setup()
scope.open_handle()
scope.set_sample_rate(sample_rate_index)
ch1 = fig.add_subplot(2,1,1)

scope.set_ch1_voltage_range(voltage_range)
scope.set_ch1_ac_dc( scope.DC )
scope.set_calibration_frequency( cal_freq )
time.sleep( 1 )
ch1_data, _ = scope.read_data(data_points)#,raw=True)#timeout=1)
voltage_data = scope.scale_read_data(ch1_data[skip:], voltage_range)
timing_data, _ = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)

scope.close_handle()
if len(timing_data) != len(voltage_data):
    w = sys.stderr.write
    w('data lengths differ!\n')
    w(str([(s,len(eval(s+'_data')))for s in 'timing voltage'.split()]))
    w('\n')
    exit(1)

with open('/tmp/scopevis.dat', 'wt') as ouf:
    ouf.write('\n'.join('{:8f}'.format(v) for v in voltage_data))
    ouf.write('\n')



##ch-2
scope = Oscilloscope()
scope.setup()
scope.open_handle()
scope.set_sample_rate(sample_rate_index)
ch2 = fig.add_subplot(2,1,2)

scope.set_ch2_voltage_range(voltage_range)
scope.set_ch2_ac_dc( scope.DC )
scope.set_calibration_frequency( cal_freq )
time.sleep( 1 )

ch2_data, _ = scope.read_data(data_points)#,raw=True)#timeout=1)
voltage_data = scope.scale_read_data(ch2_data[skip:], voltage_range)
timing_data, _ = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)
scope.close_handle()

if len(timing_data) != len(voltage_data):
    w = sys.stderr.write
    w('data lengths differ!\n')
    w(str([(s,len(eval(s+'_data')))for s in 'timing voltage'.split()]))
    w('\n')
    exit(1)

# store the data
with open('/tmp/scopevis.dat', 'wt') as ouf:
    ouf.write('\n'.join('{:8f}'.format(v) for v in voltage_data))
    ouf.write('\n')



#plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    #dummy random values
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
####################################
    scope = Oscilloscope()
    scope.setup()
    scope.open_handle()
    scope.set_sample_rate(sample_rate_index)
    scope.set_ch1_voltage_range(voltage_range)
    scope.set_ch1_ac_dc( scope.DC )
    scope.set_calibration_frequency( cal_freq )
    time.sleep( 1 )

    ch1_data, _ = scope.read_data(data_points)#,raw=True)#timeout=1)
    voltage_data = scope.scale_read_data(ch1_data[skip:], voltage_range)
    timing_data, _ = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)
    ch1.cla()
    ch1.grid()
    ch1.text(0.75,0.80,'Amplitude:'+'V',transform=ch1.transAxes)
    ch1.text(0.75,0.65,'Frequency:'+'Hz',transform = ch1.transAxes)
    ch1.set_title("Sender(CH-1)")
    ch1.set_ylabel("Amplitude")
    ch1.set_xlabel("Time(s)")
    ch1.plot(timing_data,voltage_data)

    scope.close_handle()

    scope = Oscilloscope()
    scope.setup()
    scope.open_handle()
    scope.set_sample_rate(sample_rate_index)
    scope.set_ch2_voltage_range(voltage_range)
    scope.set_ch2_ac_dc( scope.DC )
    scope.set_calibration_frequency( cal_freq )
    time.sleep( 1 )

    ch2_data, _ = scope.read_data(data_points)#,raw=True)#timeout=1)
    voltage_data2 = scope.scale_read_data(ch2_data[skip:], voltage_range)
    timing_data2, _ = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)
    ch2.cla()
    ch2.grid()
    ch2.text(0.75,0.80,'Amplitude:'+'V',transform=ch2.transAxes)
    ch2.text(0.75,0.65,'Frequency:'+'Hz',transform = ch2.transAxes)
    ch2.set_title("Receiver(CH-2)")
    ch2.set_ylabel("Amplitude")
    ch2.set_xlabel("Time(s)")
    ch2.plot(timing_data2,voltage_data2,color = 'green')



    scope.close_handle()

   

#cache_frame_data = False
#save_count = MAX_FRAMES
ani = FuncAnimation(plt.gcf(),animate,interval =1000)

plt.tight_layout()
plt.show()


