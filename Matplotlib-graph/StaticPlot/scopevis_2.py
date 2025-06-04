#!/usr/bin/python3

__author__ = 'Robert Cope'

from PyHT6022.LibUsbScope import Oscilloscope
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
nchannels=2

#sample_rate_index
#1 <->   1 MS/s
#2 <->   2 MS/s
#3 <->   3 MS/s
#4 <->   4 MS/s
#5 <->   5 MS/s
#6 <->   6 MS/s
#8 <->   8 MS/s
#10 <->  10 MS/s
#12 <->  12 MS/s
#15 <->  15 MS/s
#16 <->  16 MS/s
#24 <->  24 MS/s
#30 <->  30 MS/s
#48 <->  48 MS/s



# skip first samples due to unstable xfer
skip = 2 * 0x400 
data_points = skip + 20 * 0x400

scope = Oscilloscope()
scope.setup()
scope.open_handle()
scope.set_num_channels(2)
scope.set_sample_rate(sample_rate_index)
scope.set_ch2_voltage_range(voltage_range)
scope.set_ch2_ac_dc( scope.DC )
scope.set_calibration_frequency( cal_freq )

time.sleep( 1 )

ch2_data, a = scope.read_data(data_points)#,raw=True,timeout=1)
print(ch2_data[:10])
print("\n")
print(a[:10])
#voltage_data = scope.scale_read_data(ch2_data,1,1,1,0)
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

pylab.title('Scope Visualization Example')
pylab.plot(timing_data, voltage_data, color='#009900', label='Raw Trace')
pylab.plot(timing_data, apply_data_smoothing(voltage_data, window=3), color='#0033CC', label='Smoothed Trace')
pylab.xlabel('Time (s)')
pylab.ylabel('Voltage (V)')
pylab.grid()
pylab.legend(loc='best')
pylab.xticks(rotation=30)
pylab.tight_layout()
pylab.show()
