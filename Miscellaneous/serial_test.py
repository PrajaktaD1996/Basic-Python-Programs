#Date:30-5-23
################################################################

#serial_test.py
#################################################################

#Description
#serialy on sending eg.'<SAMPLE>'command, receiving data pkt
##################################################################


from datetime import datetime
import serial as ser
import time
import os
import signal
import logging
import serial
import numpy

name = "/dev/ttyUSB"
#s_port = ser.Serial(name+str(i), 9600, timeout=4)

s_port = ser.Serial("/dev/ttyUSB0", 9600, timeout = 4) #######
#s_port = ser.Serial("/dev/ttyUSB0", 115200, timeout = 5)   #commented 14june  #for gsm module

print(s_port.name)
                

sleep_time_s =60
product_group = "Electronic Under Test(EUT)"
#command = '<A,OUTPUT?,45890>'    #CAPVEL
#command  = '<SAMPLE>'            #CE

#command0 = 'AT\r\b'                                        #commented 14 june  #for gsm module
command1 = '<A,ABOUT>'            #VITAL_185
command2 = '<A,SAMPLE>'           #VITAL_185
baud_rate = 9600

#print("\n")

######################################for gsm module 
#print("read")
#s_port.write(command0.encode())
#at_rec =s_port.readline()
#print(at_rec)
#################################

s_port.write(command1.encode())
print("ABOUT EUT")
ser_about = s_port.readlines()    ####
print(ser_about)                  ####

time.sleep(2)
s_port.write(command2.encode())
print("Reading EUT data...")
ser_data = s_port.readlines()     ####
print(ser_data)                   ####
print("\n")

#print(ser_data.encode())
#print("ser_data")
#print("converting to string and replacing unicodes")
str_data=str(ser_data).replace('\\t',',').replace(':','-').replace('<','').replace("['",'')
#print("Splitting the data")
print("Data in Format")
data_split=str_data.split('>')
print(data_split)
#print("adding input1 and input 2")
#packet_data=data_split[0]+','+input1_state +','+input2_state
#final_packet=''.join(map(str,packet_data))
#print(final_packet)
#check=len(final_packet)
#print("length of final packet",check)
s_port.close()
print("sleeping")
#time.sleep(sleep_time_s)








         





