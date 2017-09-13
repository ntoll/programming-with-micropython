"""
Listen to a connected micro:bit for incoming messages to which you can react
as needs apply.
"""
from serial.tools.list_ports import comports as list_serial_ports
from serial import Serial


def find_microbit():
    """
    Finds the port to which the device is connected.
    """
    ports = list_serial_ports()
    for port in ports:
        # Use the vendor and product ID to identify the micro:bit.
        if "VID:PID=0D28:0204" in port[2].upper():
            return port[0]
    return None


def get_serial():
    """
    Detect if a micro:bit is connected and return a serial object to talk to
    it.
    """
    port = find_microbit()
    if port is None:
        raise IOError('Could not find micro:bit.')
    return Serial(port, 115200, timeout=1, parity='N')


serial = get_serial()  # create the serial connection to the micro:bit


# Keep listening for bytes from the device. If any are received print them.
while True:
    msg = serial.read_all()  # Remember, msg will be bytes not a string.
    if msg:
        # At this point you could check the content of msg to react in more
        # complicated ways than just printing it. For example, you could use
        # serial.write(a_response) to re-broadcast a message from the
        # micro:bit.
        print(msg)
