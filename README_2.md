# Snake and Ladder Game Package

## Overview
This is a Python-based implementation of the classic Snake and Ladder game. The game includes:

- Two players who take turns rolling a dice and moving on the board.
- The game includes snakes that move players backwards and ladders that move them forwards.
- The first player to reach position 100 wins.

## Modules
1. **Board**: Contains functions to display the board and initialize it.
2. **Game**: Controls the game flow, including rolling the dice, moving players, and checking for snakes or ladders.
3. **Players**: Manages player setup and positions.
4. **Snakes and Ladders**: Defines the snake and ladder interactions that alter player positions.
5. **Utilities**: Contains helper functions such as dice rolls.
6. **Test**: Contains TestCases for each module.


## Subpackage: Setup – Module: Board
- Rendering the game board using emojis .
- Handles the initial setup of the board
- Places snakes and ladders at predefined or randomized positions.

## Functions

- create_board: Handles the initial setup of the board, placing snakes and ladders at predefined or randomized positions. This module ensures flexibility for different game configurations.
- print_board_with_emojis: Responsible for rendering the game board using emojis. Players see an intuitive 10x10 grid with snakes (🐍), ladders (🪜), empty spaces (⬜), and player positions (🔵 for Player 1 and 🟡 for Player 2). It ensures clear visual tracking of gameplay.
- reset_board: Allow resetting the board for a new game.
- create_snakes_and_ladders: Dynamically generate random positions for snakes and ladders. (OPTIONAL)


## Subpackage: Setup – Module: Utilities

- Simulates dice rolls.
- Enhances the visual appeal with ASCII art.
- Update board and maintain a clean environment.


## Functions

- display_ascii_art: Enhances the visual appeal with ASCII art for banners, welcome messages, or game-over screens. It adds charm and creativity to the gaming experience.
- roll_dice: Simulates dice rolls by generating a random number between 1 and 6, determining how far a player moves.
- update_board_with_positions: Updates the board with new player positions.

## Sub-Package: Brain - Module 1: Game

- The core module that drives gameplay.
- Player initialization, including starting positions and progress tracking.
- Manages player turns, dice rolls, position updates, and interactions with snakes and ladders. 


## Functions

- create_players: Create the players.
- play_turn: It moves the player according to the dice.
- play_game: It manages player turns, dice rolls, position updates, and interactions with snakes and ladders. Players can quit at 
  any time by typing 'q'. The game announces the winner when a player reaches the 100th square.


## Sub-Package: Brain - Module 2: Snakes&Ladders

- Implements logic for interactions with snakes and ladders.

## Functions

- move_player: Implements logic for interactions with snakes and ladders. Landing on a snake sends a player back to its tail, while - landing on a ladder advances them to its top. This module ensures the unpredictability and excitement of the game.
- check_snake_or_ladder: Combines the snakes and ladders interactions into a single, more descriptive function.
- track_game_progress: Record the progress of the game and allow saving a history. 
- check_game_winner: Determine if there is a winner based on the positions.



## Usage
To start the game, simply run `play_game.py`. The game will display the board and prompt the players to roll the dice.

## Example
```bash
python game/play_game.py