import board
import audioio
import digitalio
from board import SPEAKER, SPEAKER_ENABLE

# Required for CircuitPlayground Express
speaker_enable = digitalio.DigitalInOut(SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

f = open("sound.wav", "rb")
speaker = audioio.AudioOut(SPEAKER, f)

speaker.play()
while speaker.playing:
  pass  # Block
