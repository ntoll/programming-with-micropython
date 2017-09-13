import audioio
import array
import time
import digitalio
from board import SPEAKER, SPEAKER_ENABLE

# Switch on the speaker for output.
speaker_enable = digitalio.DigitalInOut(SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

duration = 2
length = 8000 // 1760
wave = array.array("H", [0] * length)
wave[0] = int(2 ** 15 - 1)

with audioio.AudioOut(SPEAKER, wave) as speaker:
    speaker.play(loop=True)
    time.sleep(duration)
    speaker.stop()
