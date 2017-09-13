import music
from microbit import accelerometer


while True:
    music.pitch(accelerometer.get_x(), 20)
