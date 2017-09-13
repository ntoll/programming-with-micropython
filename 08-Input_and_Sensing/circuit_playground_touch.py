import neopixel
import touchio
import digitalio
from board import *


# Stops the speaker crackling when touched.
spkr = digitalio.DigitalInOut(SPEAKER_ENABLE)
spkr.switch_to_output()
spkr.value = False


np = neopixel.NeoPixel(NEOPIXEL, 10, auto_write=False)
touch_a1 = touchio.TouchIn(A1)
touch_a3 = touchio.TouchIn(A3)
touch_a4 = touchio.TouchIn(A4)
touch_a6 = touchio.TouchIn(A6)


while True:
    if touch_a4.value:
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
    if touch_a6.value:
        np[3] = (0, 255, 0)
        np[4] = (0, 255, 0)
    if touch_a1.value:
        np[5] = (255, 255, 0)
        np[6] = (255, 255, 0)
    if touch_a3.value:
        np[8] = (0, 0, 255)
        np[9] = (0, 0, 255)
    for j in range(10):
        np[j] = tuple((max(0, val - 32) for val in np[j]))
    np.write()
