import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD


    # TODO: read threshold from potentiometer

    
    # TODO: format LCD text according to threshhold
    distance = grovepi.digitalRead(ultrasonic_ranger) # thresh between 0, 1023
    thresh = int((grovepi.analogRead(potentiometer)/1023.0)*517) # map to between 0, 517

    obj_pres =  "OBJ PRES" if (distance < thresh) else ""
    setText(str(thresh) + "cm" +  obj_pres +"\n" + str(distance) + "cm")

    if(distance < thresh):
      setRGB(255,0,0)
    else:
      setRGB(0,255,0)

    time.sleep(0.3)
  
    
  except IOError:
    print("Error")