# Taken from the REPL based example.
from board import D13
import digitalio
import time

led = digitalio.DigitalInOut(D13)
led.switch_to_output()
while True:
    led.value = not led.value
    time.sleep(0.5)
