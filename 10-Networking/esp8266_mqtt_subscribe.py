import time
import ubinascii
import machine
from umqtt.simple import MQTTClient


def callback(topic, message):
    """
    Received messages are processed by this callback.
    """
    print((topic, message))


broker_address = '192.168.1.35'
client_id = 'esp8266_{}'.format(ubinascii.hexlify(machine.unique_id()))
topic = b'button'

client = MQTTClient(client_id, broker_address)
client.set_callback(callback)
client.connect()
client.subscribe(topic)

while True:
    client.wait_msg()
