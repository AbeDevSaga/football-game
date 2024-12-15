# Class for Ball logic (movement, collision, etc.)
from graphics import *
import random

class Ball:
    def __init__(self, window, x, y):
        """Initialize the ball at (x, y)"""
        self.x = x
        self.y = y
        self.dx = random.choice([-4, 4])  # Ball moves randomly in x direction
        self.dy = random.choice([-2, 2])  # Ball moves randomly in y direction
        self.window = window
        self.circle = Circle(Point(self.x, self.y), 15)
        self.circle.setFill('white')
        self.circle.draw(window)

    def move(self):
        """Move the ball and bounce off walls"""
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - 15 <= 0 or self.x + 15 >= 800:
            self.dx *= -1
        if self.y - 15 <= 0 or self.y + 15 >= 400:
            self.dy *= -1

        self.circle.move(self.dx, self.dy)
