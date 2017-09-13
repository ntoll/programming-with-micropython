from microbit import *


position = 2


while True: # event loop
    sleep(60) # pause
    if button_a.is_pressed():
        display.clear()
        position = max(0, position - 1)
    elif button_b.is_pressed():
        display.clear()
        position = min(4, position + 1)
    display.set_pixel(position, 2, 9)
