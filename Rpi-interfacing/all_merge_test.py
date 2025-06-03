import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
import serial
import time 

ser = serial.Serial("/dev/ttyAMA0",baudrate = 9600,parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS,timeout = 1)

counter = 0

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)


#variable should be globally defined not in class otherwisde it should be accesed

var = 1

class led1:
      def ledb(self):
          var = 1
          print("in led 1 block")
          GPIO.output(19,GPIO.HIGH)
          sleep(2)
          GPIO.output(19,GPIO.LOW)
          sleep(2)

class led2:
    def ledb2(self):
        var = 2
        print("in led 2 block")
        GPIO.output(10, GPIO.HIGH)
        sleep(2)
        GPIO.output(10,GPIO.LOW)
        sleep(2)

def __init__(self):
    pass
   # b1 = self.led1()
    #b2 = self.led2()

b1=led1()
b2=led2()


#if uart terminal sent some option to print led output
while True:
    if var == 1:
        print("in 1")
    ser.write(b'write counter: %d \n'%(counter))
    print("Printed:%d\n"%(counter))  #iteration reading getting here....
    time.sleep(1)
    counter +=1
   
    
    
    #if var == 1:
       #print("in 1")



#import time

#ser = serial.Serial("/dev/ttyAMA0",baudrate = 9600,parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS,timeout = 1)

#counter = 0

#while 1:
    #ser.write(b'write counter: %d \n'%(counter))
    #print("Printed:%d\n"%(counter))  #iteration reading getting here....
    #time.sleep(1)
    #counter +=1




#!/usr/bin/env python
#import time
#import serial
#ser = serial.Serial(
#port='/dev/ttyAMA0',
#baudrate = 9600,
#parity=serial.PARITY_NONE,
#stopbits=serial.STOPBITS_ONE,
#bytesize=serial.EIGHTBITS,
#timeout=1
#)

#while 1:
   #x=ser.readline()
   #print(x)

