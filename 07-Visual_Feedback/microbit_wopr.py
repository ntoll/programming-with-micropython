from microbit import *
import random
import array


def animation():
    blinkenlights = array.array('b', [random.randint(0, 9) for i in range(25)])
    yield Image(5, 5, blinkenlights)

    
while True:
    display.show(animation())
