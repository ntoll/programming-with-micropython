from microbit import *


while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.ANGRY)
    elif accelerometer.was_gesture('face up'):
        display.show(Image.ASLEEP)
    elif accelerometer.was_gesture('up'):
        display.show(Image.HAPPY)
    sleep(100)
