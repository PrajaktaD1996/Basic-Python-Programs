import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

#try:
while True:
      button_state = GPIO.input(23)
      GPIO.output(24,True)
      if button_state == True:
         GPIO.output(24,False)
         sleep(2)
       
       
           
           
       
           
  

