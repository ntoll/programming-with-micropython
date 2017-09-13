import lcd160cr


lcd = lcd160cr.LCD160CR('X')
lcd.erase()
lcd.write('Hello, World!')
