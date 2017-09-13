import neopixel
import random
import time
from board import NEOPIXEL


np = neopixel.NeoPixel(NEOPIXEL, 10, auto_write=False)
step = 32


while True:
    for i in range(10):
        for j in range(10):
            np[j] = tuple((max(0, val - step) for val in np[j]))
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        np[i] = (r, g, b)
        np.write()
        time.sleep(0.05)
