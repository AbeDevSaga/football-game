from graphics import Line, Point

class Goal:
    def __init__(self, window):
        """Create goal lines at the top and bottom of the screen."""
        self.top_line = Line(Point(0, 5), Point(800, 5))  # Top goal line
        self.bottom_line = Line(Point(0, 395), Point(800, 395))  # Bottom goal line
        self.top_line.setWidth(3)
        self.bottom_line.setWidth(3)
        self.top_line.setFill('white')
        self.bottom_line.setFill('white')
        self.top_line.draw(window)
        self.bottom_line.draw(window)

    def check_goal(self, ball):
        """Check if the ball crosses the goal line."""
        ball_center = ball.get_center()
        if ball_center.getY() <= 5:  # Ball crosses the top goal line
            return "player1"
        elif ball_center.getY() >= 395:  # Ball crosses the bottom goal line
            return "player2"
        return None
