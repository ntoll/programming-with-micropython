import pyb


led = pyb.LED(1)
sw = pyb.Switch()
while True:
    pyb.delay(100)
    if sw():
        led.toggle()
