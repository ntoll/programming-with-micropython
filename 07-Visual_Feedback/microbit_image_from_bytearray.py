from microbit import display, Image

buf = bytearray(x % 10 for x in range(100))
i = Image(10, 10, buf)

display.show(i.crop(3, 4, 5, 5))
