# Turtle Crossing Game

The Turtle Crossing Game is an interactive arcade-style game where the player controls a turtle aiming to cross a busy road while avoiding incoming traffic. The game is implemented using the Turtle graphics library in Python.

## How to Play

1. Use the **Up Arrow Key** to move the turtle forward.
2. Avoid colliding with the moving cars on the road.
3. Successfully cross the road and reach the finish line to level up.
4. The game will become progressively challenging as the level increases, with faster-moving cars.

## Features

- The player-controlled turtle can move forward to cross the road.
- The game features multiple lanes of moving cars that the player must avoid.
- The level of difficulty increases as the player successfully crosses the road, leading to faster car movement.
- The game displays the current level and provides a "Game Over" message when the player collides with a car.

## Files

- **main.py:** The main script that initializes the game environment, manages gameplay, and user interaction.
- **player.py:** Defines the behavior and properties of the player-controlled turtle.
- **car_manager.py:** Contains the CarManager class responsible for managing the behavior of the moving cars.
- **scoreboard.py:** Implements the Scoreboard class, which displays the current level and game over messages.

## Dependencies

- Turtle Graphics Library: The game uses the Turtle graphics library to create the graphics and animations.
