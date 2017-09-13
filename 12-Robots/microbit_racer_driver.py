from microbit import *
import radio
import neopixel


display.show(Image.SKULL)  # Logo :-)

colour = (244, 0, 244)  # NeoPixel colour to use for lights.
np = neopixel.NeoPixel(pin13, 12)
lights = False

radio.config(channel=44)
radio.on()


def move(speed, steer):
    # Sensible defaults that mean "stop".
    forward = 0
    left = 0
    right = 0
    if speed > 0:
        # Moving forward.
        forward = 1
        left = 1000 - speed
        right = 1000 - speed
    elif speed < 0:
        # In reverse.
        left = 1000 + (-1000 - speed)
        right = 1000 + (-1000 - speed)
    if steer < 0:
        # To the right.
        right = min(1000, right + abs(steer))
        left = max(0, left - abs(steer))
    elif steer > 0:
        # To the left.
        left = min(1000, left + steer)
        right = max(0, right - steer)
    # Write to the motors.
    pin8.write_digital(forward)
    pin12.write_digital(forward)
    pin0.write_analog(left)
    pin1.write_analog(right)


while True:
    pin14.write_digital(0)  # Switch off the horn
    try:
        msg = radio.receive()
    except:
        msg = None  # Networks are not safe!
    if msg is not None:
        # Get data from the incoming message.
        speed, steer, horn, light = [int(val) for val in msg.split(':')]
        move(speed, steer)  # Move the robot.
        if horn:
            # Sound the horn
            pin14.write_digital(1)
        if light:
            # Toggle lights
            if lights:
                np.clear()
                lights = False
            else:
                lights = True
                for i in range(12):
                    np[i] = colour
                    np.show()
    else:
        # No message? Do nothing!
        move(0, 0)
    sleep(20)
