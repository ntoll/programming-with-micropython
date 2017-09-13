from machine import Pin


led = Pin(2, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)


while True:
    led.value(button.value())    
