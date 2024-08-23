import time, random, micropython_dotstar as dotstar
from machine import Pin, SPI

spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
dots = dotstar.DotStar(spi, 48, brightness=0.2)
n_dots = len(dots)
delay = 0.1

while True:
    for i in range(12):
        rand_pixel = random.randint(0,n_dots-1)
        rand_colour = (random.randint(0,254),random.randint(0,254),random.randint(0,254))
        #time.sleep(delay)
        dots[rand_pixel] = rand_colour
    time.sleep(delay)
    for i in range(n_dots):
        dots[i] = (0,0,0)
    time.sleep(delay)