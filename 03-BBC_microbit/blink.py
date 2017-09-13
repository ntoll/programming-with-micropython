from microbit import display, sleep


while True:
    display.set_pixel(2, 2, 9)
    sleep(500)
    display.set_pixel(2, 2, 0)
    sleep(500)
