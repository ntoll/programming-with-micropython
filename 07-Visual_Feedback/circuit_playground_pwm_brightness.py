# Taken from the REPL based example.
from board import D13
import time
import pulseio


pin = pulseio.PWMOut(D13)


while True:
    for i in range(16):
        pin.duty_cycle = 2 ** i
        time.sleep(0.1)
