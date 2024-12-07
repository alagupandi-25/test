import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)

while True:
    if GPIO.input(8) == 0:
        print("object dected")
        time.sleep(1)
    else : 
        print("object dected")
        time.sleep(1)
