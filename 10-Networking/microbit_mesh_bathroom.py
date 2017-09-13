import radio
from microbit import *

radio.config(length=64)
radio.on()

device_name = "Bathroom"

messages = [
    "Need more toilet roll.",
    "Run out of soap.",
    "Blocked drain.",
    "Missing toothbrush.",
    "The shower is free.",
    "Yes",
    "No",
]

message_cache = {}
cache_lifetime = 1000 * 5  # 5 seconds

position = 0

while True:
    sleep(20)
    # Sweep and clean the cache of stale messages.
    now = running_time()
    to_delete = []
    # Sweep.
    for key, timestamp in message_cache.items():
        # Check the age of the cached message.
        if now > timestamp + cache_lifetime:
            to_delete.append(key)
    # Clean the cache of out stale messages.
    for stale_message in to_delete:
        del message_cache[stale_message]
    # Cycle through the available messages.
    if button_a.was_pressed():
        position += 1
        # Skip back to the beginning if we reach the end.
        if position == len(messages):
            position = 0
        # Preview the newly selected message.
        display.scroll(messages[position], 50, wait=False)
    # Send the currently selected message.
    if button_b.was_pressed():
        # Message format is "sender:content".
        radio.send('{}:{}'.format(device_name, messages[position]))
    # Check for and display incoming message, rebroadcast if required.
    msg = radio.receive()
    if msg:
        if msg not in message_cache:
            # This is a new message, so store it in the cache.
            message_cache[msg] = running_time()
            # Rebroadcast it.
            radio.send(msg)
            # Display it in a friendly way.
            sender, message = msg.split(':')
            display.scroll('{} says: {}'.format(sender, message), 50,
                           wait=False)
