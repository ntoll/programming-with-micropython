from microbit import *
import radio


radio.config(channel=42)
radio.on()


while True:
    sleep(20)
    if button_a.was_pressed():
        radio.send("Hello")
    msg = radio.receive()
    if msg:
        display.scroll(msg, 80, wait=False)
