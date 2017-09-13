import music
from microbit import accelerometer

buckets = [
    262,  # C
    294,  # D
    330,  # E
    392,  # G
    440,  # A
]

while True:
    reading = abs(accelerometer.get_x())
    bucket = min(4, max(0, reading // 200))  # quantize!
    music.pitch(buckets[bucket], 20)
