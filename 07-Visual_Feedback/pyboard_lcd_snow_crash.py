import lcd160cr
import random


lcd = lcd160cr.LCD160CR('X')
lcd.erase()


while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = lcd.rgb(r, g, b)
    x = random.randint(0, lcd.w)
    y = random.randint(0, lcd.h)
    lcd.set_pixel(x, y, colour)
