import machine, neopixel, time, random
np = neopixel.NeoPixel(machine.Pin(16), 12)
delay = 0.2
while True:
    for i in range(3):
        rand_pixel = random.randint(0,11)
        rand_colour = (random.randint(0,254),random.randint(0,254),random.randint(0,254))
        time.sleep(delay)
        np[rand_pixel] = rand_colour
        np.write()
    time.sleep(delay)
    for i in range(12):
        np[i] = (0,0,0)
        np.write()
    time.sleep(delay)
