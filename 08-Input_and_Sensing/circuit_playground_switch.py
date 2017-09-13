import neopixel
import time
import digitalio
from board import NEOPIXEL, SLIDE_SWITCH


np = neopixel.NeoPixel(NEOPIXEL, 10, auto_write=False)
switch = digitalio.DigitalInOut(SLIDE_SWITCH)
switch.pull = digitalio.Pull.UP


while True:
    time.sleep(0.05)
    for i in range(10):
        if switch.value:
            i = 9 - i
        for j in range(10):
            np[j] = tuple((max(0, val - 64) for val in np[j]))
        np[i] = (0, 0, 254)
        np.write()
