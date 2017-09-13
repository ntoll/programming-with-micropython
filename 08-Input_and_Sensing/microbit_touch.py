from microbit import display, Image, pin0


while True:
    display.show(Image.ASLEEP)
    if pin0.is_touched():
        display.show(Image.HAPPY)
