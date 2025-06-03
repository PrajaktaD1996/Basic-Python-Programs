import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)

class led1:
      def ledb(self):
          print("in led 1 block")
          GPIO.output(19,GPIO.HIGH)
          sleep(2)
          GPIO.output(19,GPIO.LOW)
          sleep(2)

class led2:
    def ledb2(self):
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
while True:
    b1.ledb()
    #sleep(2)
    b2.ledb2()
    #sleep(2)
        



