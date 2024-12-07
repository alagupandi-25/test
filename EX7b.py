import time 

bp = '/sys/class/leds/ACT/brightness'

def setled(value):
    with open(bp,"w") as f:
        f.write(value)

while True:
    for i in range(0,256):
        setled(i)
        time.sleep(0.5)

    for i in range(255,-1,-1):
        setled(i)
        time.sleep(0.5)
        