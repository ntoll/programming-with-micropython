from microbit import *
import radio


radio.config(channel=44)
radio.on()


# Defines the range of valid tilt from accelerometer readings.
max_tilt = 1000
min_tilt = 199


while True:
    # Grab the inputs.
    y = accelerometer.get_y()  # Forwards / backwards.
    x = accelerometer.get_x() # Left / right.
    a = button_a.was_pressed()  # Horn.
    b = button_b.was_pressed()  # Toggle lights.

    # Data from the controller to be sent to the vehicle.
    # [speed, steer, buzzer, neopixel]
    control_data = [0, 0, 0, 0]
    if x < -min_tilt and y < -min_tilt:
        # forwards left
        display.show(Image.ARROW_NW)
        control_data[0] = max(y, -max_tilt)
        control_data[1] = max(x, -max_tilt)
    elif x < -min_tilt and y > min_tilt:
        # backwards left
        display.show(Image.ARROW_SW)
        control_data[0] = min(y, max_tilt)
        control_data[1] = max(x, -max_tilt)
    elif x > min_tilt and y < -min_tilt:
        # forwards right
        display.show(Image.ARROW_NE)
        control_data[0] = max(y, -max_tilt)
        control_data[1] = min(x, max_tilt)
    elif x > min_tilt and y < min_tilt:
        # backwards right
        display.show(Image.ARROW_SE)
        control_data[0] = min(y, max_tilt)
        control_data[1] = min(x, max_tilt)
    elif y > min_tilt:
        # backwards
        display.show(Image.ARROW_S)
        control_data[0] = min(y, max_tilt)
    elif y < -min_tilt:
        # forwards
        display.show(Image.ARROW_N)
        control_data[0] = max(y, -max_tilt)
    if a:
        # Sound the buzzer 
        control_data[2] = 1
    if b:
        # Toggle the NeoPixels 
        control_data[3] = 1
    if any(control_data):
        msg = '{}:{}:{}:{}'.format(*control_data)
        radio.send(msg)
    else:
        display.clear()
    sleep(20)
