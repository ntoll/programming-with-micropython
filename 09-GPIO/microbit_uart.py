from microbit import *


while True:
    msg = uart.read()
    if msg:
        uart.write(msg)
