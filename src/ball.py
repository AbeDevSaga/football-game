from graphics import Circle, Point

class Ball:
    def __init__(self, window, x, y):
        """Create a ball at position (x, y)."""
        self.shape = Circle(Point(x, y), 10)
        self.shape.setFill('white')
        self.shape.draw(window)
        self.dx = 0  # Initial x velocity
        self.dy = 0  # Initial y velocity
        self.window = window

    def move(self):
        """Move the ball according to its velocity."""
        self.shape.move(self.dx, self.dy)
        center = self.shape.getCenter()
        
        # Check if the ball hits the side walls, bounce it back
        if center.getX() <= 10 or center.getX() >= 790:  # Bounce from side walls
            self.dx = -self.dx

    def kick(self, dx, dy):
        """Set the ball in motion."""
        self.dx = dx
        self.dy = dy

    def stop(self):
        """Stop the ball's movement."""
        self.dx = 0
        self.dy = 0

    def get_center(self):
        """Return the center point of the ball."""
        return self.shape.getCenter()

    def reset_position(self, x, y):
        """Reset the ball's position to the given (x, y) and stop it."""
        self.shape.undraw()
        self.shape = Circle(Point(x, y), 10)
        self.shape.setFill('white')
        self.shape.draw(self.window)
        self.stop()
