import time 

bp = '/sys/class/leds/ACT/brightness'

def setled(value):
    with open(bp,"w") as f:
        f.write(value)

while True:
    setled(1)
    time.sleep(1)
    setled(0)
    time.sleep(1)