import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)
while True: # Run forever
    led1()

def led1():
    GPIO.output(10,GPIO.HIGH)
    sleep(2)
    GPIO.output(10,GPIO.LOW)
    sleep(2)

def led2():
    GPIO.output(19,GPIO.HIGH)
    sleep(2)
    GPIO.output(19,GPIO.LOW)
    sleep(2)



