# Functions for loading images, sounds, etc.
from graphics import *

def load_image(path, x, y):
    """Load an image and place it at x, y"""
    image = Image(Point(x, y), path)
    return image
