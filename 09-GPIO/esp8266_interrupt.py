from machine import Pin


def callback(p):
    print('Pin', o)


p0 = Pin(0, Pin.IN)
p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)
