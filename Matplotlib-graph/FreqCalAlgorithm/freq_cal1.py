##sample code for calculating frequency 
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

frequency = 2
amp = 1




#print(frequency)

sampling_rate = 100
duration = 1

t = np.arange(0, duration,1/sampling_rate)
sine_wav = amp*np.sin(2*np.pi*frequency*t)

#peaks = find_peaks(sine_wav,height=1,threshold = 1,distance=1)
#print("peaks=",peaks)
#height = peaks[-1]['peak_heights']
#print("height=",height)
#peak_pos= t[peaks[-1]]
#print("peak_pos=",peak_pos)



plt.plot(t,sine_wav)
plt.xlabel('Time(s)')
plt.ylabel('Amplitute')
plt.show()
