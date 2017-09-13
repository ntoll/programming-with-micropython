import speech
from microbit import sleep, button_a, button_b, display, Image

gap = 220  # How long a silence should be.
bass_drum = "BUH"  # Sound of a beat box bass drum
snare = "CHIXIX"  # Sound of a beat box snare
roll = "DGDG"  # Sound of a beat box drum roll
rest = ""  # Represents a rest of "gap" duration

# Two sequences (lists) of beats. One beat per line.
beats1 = [  # Mellow
    bass_drum, rest, rest, rest,
    snare, rest, rest, rest,
    bass_drum, bass_drum, bass_drum, rest,
    snare, rest, roll, roll,
]

beats2 = [  # Hardcore
    bass_drum, snare, snare, snare,
    bass_drum, snare, roll, roll,
    bass_drum, bass_drum, bass_drum, snare,
    bass_drum, roll, roll, bass_drum,
]

# Play a sound or silence.
def beat_box(sound):
    if sound:
        display.show(Image.HEART)
        sleep(10)
        display.clear()
        speech.pronounce(sound)
    else:
        sleep(gap)

# Play all sounds in "beats" sequence.
def play(beats):
    for beat in beats:
        beat_box(beat)

selected = beats1  # Default beat sequence
# Keep on looping over the selected sequence
while True:
    # Change sequence with buttons A and B
    if button_a.was_pressed():
        selected = beats1
    elif button_b.was_pressed():
        selected = beats2
    # Finally play the selected sequence
    play(selected)
