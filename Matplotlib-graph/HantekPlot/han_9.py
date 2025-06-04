##getting real time hantek graph



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

sample_rate_index = 1
voltage_range = 0x01
cal_freq = 10
skip = 2 * 0x400
data_points = skip + 20 * 0x400

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
    #scope.close_handle()

###########################################    


   
    
    plt.cla()
    #dummy random values
    ##plt.plot(x_vals,y_vals)
    plt.plot(timing_data,voltage_data)
    scope.close_handle()

   

#cache_frame_data = False
#save_count = MAX_FRAMES
ani = FuncAnimation(plt.gcf(),animate,interval =1000)

plt.tight_layout()
plt.show()


