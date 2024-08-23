import time, machine

r = machine.Pin(13, machine.Pin.OUT)
g = machine.Pin(14, machine.Pin.OUT)
b = machine.Pin(15, machine.Pin.OUT)
for i in range(100):
    r.high()
    time.sleep(1)
    r.low()
    g.high()
    time.sleep(1)
    g.low()
    b.high()
    time.sleep(1)
    b.low()
