import pyb
import random
from pyb import DAC


def volume(val):
    pyb.I2C(1, pyb.I2C.MASTER).mem_write(val, 46, 0)

volume(127)
dac = DAC(1)
while True:
    dac.write(random.randint(0, 256))
