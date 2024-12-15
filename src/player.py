# Class for Player logic (movement, rendering, etc.)
from graphics import *

class Player:
    def __init__(self, window, x, y, color):
        """Initialize the player at (x, y)"""
        self.x = x
        self.y = y
        self.window = window
        self.color = color
        self.circle = Circle(Point(self.x, self.y), 20)
        self.circle.setFill(self.color)
        self.circle.draw(window)

    def move(self, dx, dy):
        """Move the player within the window"""
        self.x += dx
        self.y += dy
        self.circle.move(dx, dy)
