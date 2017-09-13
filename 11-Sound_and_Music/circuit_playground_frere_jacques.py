import audioio
import digitalio
import array
import time
from board import SPEAKER, SPEAKER_ENABLE

# Switch on the speaker for output.
speaker_enable = digitalio.DigitalInOut(SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

notes = {
  'b': 493,
  'a#': 466,
  'a': 440,
  'g#': 415,
  'g': 392,
  'f#': 370,
  'f': 347,
  'e': 330,
  'd#': 311,
  'd': 294,
  'c#': 277,
  'c': 262,
}


def bloop(pitch, duration):
    length = 8000 // pitch
    wave = array.array("H", [0] * length)
    wave[0] = int(2 ** 16 - 1)
    with audioio.AudioOut(SPEAKER, wave) as speaker:
        speaker.play(loop=True)
        time.sleep(duration - 0.01)
        speaker.stop()
        time.sleep(0.01)  # add articulation silence


def play(tune):
    for note in tune:
        name, duration = note.split(':')
        bloop(notes[name], int(duration) / 8)

line1 = ['c:4', 'd:4', 'e:4', 'c:4']
line2 = ['e:4', 'f:4', 'g:8']
line3 = ['g:2', 'a:2', 'g:2', 'f:2', 'e:4', 'c:4']
line4 = ['c:4', 'g:4', 'c:8']
frere_jacques = line1 * 2 + line2 * 2 + line3 * 2 + line4 * 2

play(frere_jacques)
