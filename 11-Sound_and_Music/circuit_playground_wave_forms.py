import audioio
import digitalio
import time
import array
import math
from board import SPEAKER, SPEAKER_ENABLE


# Switch on the speaker for output.
speaker_enable = digitalio.DigitalInOut(SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

length = 8000 // 440
sine = array.array("H", [0] * length)
triangle = array.array("H", [0] * length)
sawtooth = array.array("H", [0] * length)
square = array.array("H", [0] * length)


# The waveforms are created here.
for i in range(length):
    sine[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15 - 1) + (2 ** 15))
    triangle[i] = abs(int(i * ((2 ** 15 - 1) // length)) - 2 ** 14)
    sawtooth[i] = int(i * ((2 ** 15 - 1) // length))
    if i < length // 2:
        square[i] = (2 ** 16 -1)


# Play each waveform.
print("Sine")
with audioio.AudioOut(SPEAKER, sine) as sample:
    sample.play(loop=True)
    time.sleep(2)
    sample.stop()

print("Triangle")
with audioio.AudioOut(SPEAKER, triangle) as sample:
    sample.play(loop=True)
    time.sleep(2)
    sample.stop()

print("Sawtooth")
with audioio.AudioOut(SPEAKER, sawtooth) as sample:
    sample.play(loop=True)
    time.sleep(2)
    sample.stop()

print("Square")
with audioio.AudioOut(SPEAKER, square) as sample:
    sample.play(loop=True)
    time.sleep(2)
    sample.stop()
