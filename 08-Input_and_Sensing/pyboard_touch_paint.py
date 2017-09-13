import lcd160cr


lcd = lcd160cr.LCD160CR('X')
lcd.erase()


while True:
    a, x, y = lcd.get_touch()
    if a:
        lcd.set_pixel(x, y, lcd.rgb(255, 255, 255))
