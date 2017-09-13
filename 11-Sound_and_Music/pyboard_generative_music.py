import pyb
from pyb import DAC


def volume(val):
    pyb.I2C(1, pyb.I2C.MASTER).mem_write(val, 46, 0)

volume(127)
dac = DAC(1)
t = 0
while True:
    dac.write(int(t*((t>>9|t>>13)&25&t>>6)) % 256)
    #dac.write(int(t*((15&t>>11)%12)&55-(t>>5|t>>12)|t*(t>>10)*32) % 256)
    #dac.write(int((t*9&t>>4|t*5&t>>7|t*3&t//1024)-1))
    t += 1

