import os
from gpiozero import MotionSensor
 
def mypic():
    t="fswebcam -F 5 --fps 20 -r \"1200x800\" /home/pi/cam/imgs/cod.jpg"
    os.system(t)
 
 
def mytweet():
    print("mypic")
    
 
 
pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        mypic()
        print("Motion detected!")
