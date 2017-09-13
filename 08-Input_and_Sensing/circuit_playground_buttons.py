import neopixel
import time
import digitalio
from board import NEOPIXEL, BUTTON_A, BUTTON_B


np = neopixel.NeoPixel(NEOPIXEL, 10, auto_write=False)
button_a = digitalio.DigitalInOut(BUTTON_A)
button_a.pull = digitalio.Pull.DOWN
button_b = digitalio.DigitalInOut(BUTTON_B)
button_b.pull = digitalio.Pull.DOWN


clockwise = True


while True:
    time.sleep(0.05)
    if button_a.value:
        clockwise = True
    elif button_b.value:
        clockwise = False
    for i in range(10):
        if clockwise:
            i = 9 - i
        for j in range(10):
            np[j] = tuple((max(0, val - 64) for val in np[j]))
        np[i] = (0, 0, 254)
        np.write()
