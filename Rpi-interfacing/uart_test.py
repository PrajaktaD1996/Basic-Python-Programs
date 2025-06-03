import time 
import serial

ser = serial.Serial("/dev/ttyAMA0",baudrate = 9600,parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS,timeout = 1)

counter = 0

while 1:
    ser.write(b'write counter: %d \n'%(counter))
    print("Printed:%d\n"%(counter))  #iteration reading getting here....
    time.sleep(1)
    counter +=1




#!/usr/bin/env python
import time
import serial
ser = serial.Serial(
port='/dev/ttyAMA0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

while 1:
    x=ser.readline()
    print(x)
