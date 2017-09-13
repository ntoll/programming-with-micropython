import neopixel
import audiobusio
import digitalio
import audioio
import time
from board import *


def countdown(np):
    """ Uses the NeoPixels to display a countdown."""
    # Start from an "off" state.
    np.fill((0, 0, 0))
    np.write()
    for i in range(10):
        np[i] = (0, 20, 0)
        np.write()
        time.sleep(0.5)
    np.fill((0, 128, 0))
    np.write()


def record():
    """ Returns a buffer of recorded sound."""
    buf = bytearray(8000)
    with audiobusio.PDMIn(MICROPHONE_CLOCK, MICROPHONE_DATA) as mic:
        mic.record(buf, len(buf))
    return buf


def play(buf, freq):
    """
    Play the referenced buffer of recorded sound at a certain
    frequency.
    """
    # Set the speaker ready for output.
    speaker_enable = digitalio.DigitalInOut(SPEAKER_ENABLE)
    speaker_enable.switch_to_output(value = True)
    # Play the audio buffer through the speaker.
    with audioio.AudioOut(SPEAKER, buf) as speaker:
        speaker.frequency = freq
        speaker.play()
        # Block while the speaker is playing.
        while speaker.playing:
            pass


neopixels = neopixel.NeoPixel(NEOPIXEL, 10, auto_write=False)
button_a = digitalio.DigitalInOut(BUTTON_A)
button_a.pull = digitalio.Pull.DOWN
button_b = digitalio.DigitalInOut(BUTTON_B)
button_b.pull = digitalio.Pull.DOWN


countdown(neopixels)
audio_buffer = record()
neopixels.fill((0, 0, 0))
neopixels.write()


freq = 8000 # Default = normal speed.
if button_a.value:
    freq = 12000 # Button A = chipmunk.
elif button_b.value:
    freq = 6000 # Button B = Barry White.


play(audio_buffer, freq)
