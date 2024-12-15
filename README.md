# 2D Football Game

This is a simple 2D football game built using Python and John Zelle's `graphics.py` library.

## 📁 File Structure
📁 FootballGame 
┣ 📁 assets
┃ ┣ 🖼️ player1.png # Image for Player 1 ┃ ┣ 🖼️ player2.png #Image for Player 2 
┃ ┣ ⚽ ball.png # Image for Ball ┃ ┗ 🎵 goal_sound.wav # Sound played when a goal is scored 
┣ 📁 config
┃ ┗ constants.py # Game constants like screen size, player speed, etc. 
┣ 📁 src
┃ ┣ player.py # Class for Player logic (movement, rendering, etc.) ┃ ┣ ball.py # Class for Ball logic (movement, collision, etc.) ┃ ┣ goal.py # Handles logic for checking goals ┃ ┗ main.py # Main game loop and entry point ┣ 📁 utils
┃ ┗ helpers.py # Functions for loading images, sounds, etc. ┗ README.md # Project documentation