from microbit import *


x = 2
y = 2
sensitivity = 50
pause = 90
fade = 2


while True:
    roll = accelerometer.get_x()
    yaw = accelerometer.get_y()
    if roll < -sensitivity:
        x = max(0, x - 1)
    elif roll > sensitivity:
        x = min(4, x + 1)
    if yaw < -sensitivity:
        y = max(0, y - 1)
    elif yaw > sensitivity:
        y = min(4, y + 1)
    for i in range(5):
        for j in range(5):
            brightness = max(0, display.get_pixel(i, j) - fade)
            display.set_pixel(i, j, brightness)
    display.set_pixel(x, y, 9)
    sleep(pause)
