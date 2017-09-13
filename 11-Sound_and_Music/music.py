"""
To be copied as a module onto the Circuit Playground Express board.
"""
import audioio
import digitalio
import array
import time
from board import *

# Switch on the speaker for output.
speaker_enable = digitalio.DigitalInOut(SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

def bloop(pitch, duration):
    length = 8000 // pitch
    wave = array.array("H", [0] * length)
    wave[0] = int(2 ** 16 - 1)
    with audioio.AudioOut(SPEAKER, wave) as speaker:
        speaker.play(loop=True)
        time.sleep(duration - 0.01)
        speaker.stop()
        time.sleep(0.01)  # add articulation silence
