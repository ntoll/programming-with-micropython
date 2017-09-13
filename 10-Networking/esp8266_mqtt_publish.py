import time
import ubinascii
import machine
from umqtt.simple import MQTTClient


button = machine.Pin(0, machine.Pin.IN)

broker_address = '192.168.1.35'
client_id = 'esp8266_{}'.format(ubinascii.hexlify(machine.unique_id()))
topic = b'button'

client = MQTTClient(client_id, broker_address)
client.set_last_will(topic, b'dead')
client.connect()

while True:
    while True:
        if button.value() == 0:
            break
        time.sleep_ms(20)
    client.publish(topic, b'toggled')
    time.sleep_ms(200)

client.disconnect()
