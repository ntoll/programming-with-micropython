# Taken from the REPL based example.
import pyb


while True:
    pyb.LED(1).toggle()
    pyb.delay(500)
