import requests
import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)

URL = "http://api.thingspeak.com/update"
API_KEY = "*************"

def sendData(value):
    data = {
        'api_key':API_KEY,
        'field1':value
    }
    try:
        response = requests.post(URL,data=data)
        response.raise_for_status()
        print("data sended sucessfully")
    except requests.exceptions.RequestException:
        print("failed to send data")
    
try:
    while True:
        if GPIO.input(8) == 0:
            print("object detected")
            sendData(1)
        else : 
            print("object not detected")
            sendData(0)
        time.sleep(1)
except KeyboardInterrupt:
    print("exited")
finally:
    GPIO.cleanup()