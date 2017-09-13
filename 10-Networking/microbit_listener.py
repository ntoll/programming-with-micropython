from microbit import *
import radio

radio.on()

while True:
    radio_msg = radio.receive_bytes()
    if radio_msg:
        uart.write(radio_msg)
    pc_msg = uart.read()
    if pc_msg:
        radio.send_bytes(pc_msg)
