# Main game loop and entry point
from graphics import *
from src.player import Player
from src.ball import Ball
from src.goal import Goal

def main():
    # Create game window
    window = GraphWin("2D Football Game", 800, 400)
    window.setBackground('green')

    # Create players
    player1 = Player(window, 100, 200, 'red')
    player2 = Player(window, 700, 200, 'blue')

    # Create ball and goal lines
    ball = Ball(window, 400, 200)
    goal = Goal(window)

    score1 = 0
    score2 = 0
    score_display = Text(Point(400, 20), f"Player 1: {score1}  |  Player 2: {score2}")
    score_display.setSize(16)
    score_display.setStyle('bold')
    score_display.setTextColor('white')
    score_display.draw(window)

    while True:
        key = window.checkKey()
        
        # Player 1 controls (W/S)
        if key == "w":
            player1.move(0, -20)
        elif key == "s":
            player1.move(0, 20)

        # Player 2 controls (UP/DOWN arrows)
        elif key == "Up":
            player2.move(0, -20)
        elif key == "Down":
            player2.move(0, 20)

        ball.move()

        goal_scorer = goal.check_goal(ball)
        if goal_scorer == "player1":
            score1 += 1
            ball = Ball(window, 400, 200)
        elif goal_scorer == "player2":
            score2 += 1
            ball = Ball(window, 400, 200)

        score_display.setText(f"Player 1: {score1}  |  Player 2: {score2}")

        if key == 'q':
            break

    window.close()

if __name__ == '__main__':
    main()
