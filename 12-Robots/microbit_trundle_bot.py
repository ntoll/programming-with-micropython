import microbit

class Servo:
    def __init__(self, pin, trim=0):
        self.pin = pin
        self.trim = trim
        self.speed = 0
        self.pin.set_analog_period(20)

    def set_speed(self, speed):
        self.pin.write_analog(int(25 + 100 * (90 + speed) / 180 + self.trim))
        self.speed = speed


class Robot:
    def __init__(self):
        # Remember to check the trim values.
        self.left_servo = Servo(microbit.pin0, 2)
        self.right_servo = Servo(microbit.pin1, 1)

    def go(self, distance):
        microbit.display.show(microbit.Image.ARROW_S)
        self.left_servo.set_speed(-90)
        self.right_servo.set_speed(90)
        microbit.sleep(int(distance * 2000 / 17))
        self.stop()

    def turn(self, angle):
        if angle > 0:
            microbit.display.show(microbit.Image.ARROW_E)
            self.left_servo.set_speed(-90)
            self.right_servo.set_speed(-90)
            microbit.sleep(int(angle * 64 / 9))
        else:
            microbit.display.show(microbit.Image.ARROW_W)
            self.left_servo.set_speed(90)
            self.right_servo.set_speed(90)
            microbit.sleep(int(-angle * 64 / 9))
        self.stop()

    def stop(self):
        microbit.display.show(microbit.Image.DIAMOND)
        self.left_servo.set_speed(0)
        self.right_servo.set_speed(0)

    def get_distance(self):
        return microbit.pin2.read_analog()


robot = Robot()
while True:
    robot.go(5)
    if robot.get_distance() > 700:
        robot.turn(20)
        left_distance = robot.get_distance()
        robot.turn(-40)
        right_distance = robot.get_distance()
        robot.turn(20)
        if left_distance < right_distance:
            robot.turn(60)
        else:
            robot.turn(-60)
