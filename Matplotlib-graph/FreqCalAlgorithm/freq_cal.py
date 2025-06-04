import numpy as np 
import matplotlib.pyplot as plt
cnt = 0

frame = 1e3
#x = np.arange(0,4*np.pi,0.1)

x = np.arange(0,3*np.pi,0.01)
y = np.sin(x)
xl = len(x)
print(xl)
y_max = max(y)
print(y_max)

for i in range(xl):
    if(((round((y[i]),5))==1.00000)):
    #if(((round((y[i]),5))==1.00000)or((round((y[i]),5))==0.00000)or((round((y[i]),5))==-1.00000)):
        cnt = (x[i])*4

        print(x[i])
        #print(cnt)
        #print("\n")
        #cnt = cnt+1
        #continue



print(1/cnt)
#print(x[i])
#print(x)
#print("\n")
y_max = max(y)



#print(max(y))




#diff =  np.diff(y)
#num = np.where(diff)[0]
#tmp = len(x)
#print(tmp)
################################## freq algo
#t = np.arange(256)
#print(t.shape[-1])
#print(t.shape)
#freq = np.fft.fftfreq(t.shape[-1])
#freql = len(freq)
#print((max(freq))/2)
#############################################
#peaks, properties = find_peaks(x, prominence=1, width=20)


#peaks, _ = find_peaks(x, height=1)
#peaks, properties = find_peaks(x, prominence=1, width=20)
#properties["prominences"], properties["widths"]

#plt.vlines(x=peaks, ymin=x[peaks] - properties["prominences"], ymax = x[peaks], color = "C1")
#plt.plot(peaks, x[peaks], "x")

#print(peaks)

#print(num)
#total = np.diff(num)#
#avg  = np.mean(total)#


#freq = frame/avg/2#

#print(freq)#

plt.plot(x, y)
#plt.plot(freq,y)
plt.show()

