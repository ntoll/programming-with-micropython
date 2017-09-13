import pyb
import lcd160cr
from random import randint, choice, uniform


lcd = lcd160cr.LCD160CR('X')


MAX_DEPTH = 4
RED = lcd.rgb(255, 0, 0)
YELLOW = lcd.rgb(255, 255, 0)
BLUE = lcd.rgb(0, 0, 255)
WHITE = lcd.rgb(255, 255, 255)
BLACK = lcd.rgb(0, 0, 0)
COLOURS = [RED, YELLOW, BLUE, WHITE, WHITE, WHITE]


class Node:
    """
    A node in a tree representation of a Mondrian painting.
    """

    def __init__(self, depth=0):
        """
        Choose the colour of the rectangle, work out the depth
        add child nodes if not too deep.
        """
        self.colour = choice(COLOURS)
        self.depth = depth + 1
        self.children = []
        if self.depth <= MAX_DEPTH:
            self.direction = choice(['h', 'v'])
            self.divide = uniform(0.1, 0.9)
            self.children.append(Node(self.depth))
            self.children.append(Node(self.depth))

    def draw(self, x, y, w, h):
        """
        Recursively draw this node and its children.
        """
        lcd.set_pen(BLACK, self.colour)
        lcd.rect(x, y, w, h)
        if self.children:
            if self.direction == 'h':
                self.children[0].draw(x, y, int(w * self.divide), h)
                self.children[1].draw(x + int(w * self.divide), y,
                                      int(w * (1.0 - self.divide)), h)
            else:
                self.children[0].draw(x, y, w, int(h * self.divide))
                self.children[1].draw(x, y + int(h * self.divide), w,
                                      int(h * (1.0 - self.divide)))


while True:
    # Keep re-drawing new Mondrian pictures every few seconds.
    tree = Node()
    tree.draw(0, 0, lcd.w, lcd.h)
    pyb.delay(randint(4000, 8000))
