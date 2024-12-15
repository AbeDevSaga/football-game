 # Handles logic for checking goals
class Goal:
    def __init__(self, window):
        """Initialize the goal lines"""
        self.top_line = Line(Point(0, 5), Point(800, 5))
        self.bottom_line = Line(Point(0, 395), Point(800, 395))
        self.top_line.setFill('yellow')
        self.bottom_line.setFill('yellow')
        self.top_line.setWidth(5)
        self.bottom_line.setWidth(5)
        self.top_line.draw(window)
        self.bottom_line.draw(window)

    def check_goal(self, ball):
        """Check if the ball crosses the goal line"""
        if ball.y - 15 <= 5:
            return "player2"
        if ball.y + 15 >= 395:
            return "player1"
        return None
