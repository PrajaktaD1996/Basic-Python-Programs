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
import keyboard
from collections import deque
#from scipy.fftpack import fft, ifft,fftfreq
#import numpy.fft as fft
#from scipy.signal import find_peaks
from datetime import datetime
#import sys

#datetime_object = datetime.now()
#print(datetime_object)
#print('Type :- ',type(datetime_object))


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
ch1_data, ch2_data = scope.read_data(data_points)#,raw=True)#timeout=1)
voltage_data = scope.scale_read_data(ch1_data[skip:], voltage_range)
tim1_data, tim2_data = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)

#print(max(freq))

###
#indices = find_peaks(timing_data)[0]
#print(indices)
###
scope.close_handle()
if len(tim1_data) != len(voltage_data):
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

ch1_data, ch2_data = scope.read_data(data_points)#,raw=True)#timeout=1)
voltage_data = scope.scale_read_data(ch2_data[skip:], voltage_range)
timing_data, tim2_data = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)
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

    datetime_object = datetime.now()
    #print(datetime_object)
    #print('Type :- ',type(datetime_object))

####################################
    scope = Oscilloscope()
    scope.setup()
    scope.open_handle()
    scope.set_sample_rate(sample_rate_index)
    scope.set_ch1_voltage_range(voltage_range)
    scope.set_ch1_ac_dc( scope.DC )
    scope.set_calibration_frequency( cal_freq )
    time.sleep( 1 )

    ch1_data, ch2_data = scope.read_data(data_points)#,raw=True)#timeout=1)
    voltage_data = scope.scale_read_data(ch1_data[skip:], voltage_range)
    timing_data, tim2_data = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)
    t1 = len(timing_data)
    A_max =round((max(voltage_data)),3)
    Amp1  = str(A_max)
    A_min = min(voltage_data)
    freq1 = 1
    for i in range(t1):
        if(voltage_data[i]==A_max):
            t11 = round((timing_data[i]),4)
            #print("t_max:",t11)
            if(t11!=0):
                f11 = 2/(t11*1)
                freq1=f11+70
        if(voltage_data[i]==A_min):
            t_min = round((timing_data[i]),4)
            
    freq1_rnd  =  round((freq1),4)
    freq1_str  =  str(freq1_rnd)

    ch1.cla()
    ch1.grid()
    ch1.text(0.70,1.05,'Amp:'+Amp1+'V',transform=ch1.transAxes)
    ##ch1.text(0.85,1.05,'Freq:'+freq1_str+'Hz',transform = ch1.transAxes)
    ch1.text(0.00,1.05,datetime_object,alpha = 0.8,transform = ch1.transAxes)

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

    ch1_data, ch2_data = scope.read_data(data_points)#,raw=True)#timeout=1)
    voltage_data = scope.scale_read_data(ch2_data[skip:], voltage_range)
    timing_data, tim2_data = scope.convert_sampling_rate_to_measurement_times(data_points-skip, sample_rate_index)
    t2 = len(timing_data)
    A2_max = round((max(voltage_data)),3)
    Amp2  = str(A2_max)
    A2_min = min(voltage_data)
    freq2 = 1
    for i in range(t2):
        if(voltage_data[i]==A2_max):
            t22 = round((timing_data[i]),4)
            #print("t_max:",t11)
            if(t22!=0):
                f22 = 2/(t22*1)
                freq2=f22+70
        if(voltage_data[i]==A2_min):
            t2_min = round((timing_data[i]),4)

    freq2_rnd  =  round((freq2),4)
    freq2_str  =  str(freq2_rnd)

    ch2.cla()
    ch2.grid()
    ch2.text(0.70,1.05,'Amp:'+Amp2+'V',transform=ch2.transAxes)
    ##ch2.text(0.85,1.05,'Freq:'+freq2_str+'Hz',transform = ch2.transAxes)
    ch2.set_title("Receiver(CH-2)")
    ch2.set_ylabel("Amplitude")
    ch2.set_xlabel("Time(s)")
    ch2.plot(timing_data,voltage_data,color = 'green')



    scope.close_handle()

   

#cache_frame_data = False
#save_count = MAX_FRAMES
##if keyboard.is_pressed('q'):
    ##print("jhjjvg")
   # break
##else:
    ##print("not")

ani = FuncAnimation(plt.gcf(),animate,interval =1000)
#anim.savefig('/home/sapuser/Documents/FIG_LOG/vital.png')

#while True: 
    #try:  
        #if keyboard.is_pressed('q'):  
            #print('You Pressed A Key!')
            #break  # finishing the loop
    #except:
        #break


plt.tight_layout()
plt.show()


