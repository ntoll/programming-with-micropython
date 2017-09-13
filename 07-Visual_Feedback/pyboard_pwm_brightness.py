# Taken from REPL based example.
import pyb


blue = pyb.LED(4)
i = 0
while True:
    pyb.delay(5)
    i += 1
    if i > 255:
        i = 0
    blue.intensity(i)
