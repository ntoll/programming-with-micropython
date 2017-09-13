import neopixel
import audioio
import digitalio
import array
import time
from board import *

np = neopixel.NeoPixel(NEOPIXEL, 10)
left = digitalio.DigitalInOut(BUTTON_A)
left.pull = digitalio.Pull.DOWN
right = digitalio.DigitalInOut(BUTTON_B)
right.pull = digitalio.Pull.DOWN

length = 8000 // 1760
wave = array.array("H", [0] * length)
wave[0] = int(2 ** 16 - 1)

# Switch on the speaker for output.
speaker_enable = digitalio.DigitalInOut(SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

speaker = audioio.AudioOut(SPEAKER, wave)
bleep_duration = 0.02
default_tempo = 0.48
tempo = default_tempo
tempo_change = 0.02

while True:
    if left.value and right.value:
        tempo = default_tempo
    elif left.value:
        tempo = min(tempo + tempo_change, 2.98)
    elif right.value:
        tempo = max(tempo - tempo_change, 0.02)
    np.fill((0, 255, 0))
    np.write()
    speaker.play(loop=True)
    time.sleep(bleep_duration)
    speaker.stop()
    np.fill((0, 0, 0))
    np.write()
    time.sleep(tempo)
