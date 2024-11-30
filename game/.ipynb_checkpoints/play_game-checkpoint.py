from snake_ladder.snakes_ladders.check_interaction import move_player
from snake_ladder.utilities.roll_dice import roll_dice
from snake_ladder.board.display import print_board_with_emojis
from snake_ladder.players.player_setup import create_players 
from snake_ladder.utilities.ascii_art import display_ascii_art



# def play_turn(player_positions, current_player, snakes, ladders):

#     """
#     Simulates a player's turn: rolling the dice, moving the player, and checking for snakes/ladders.
    
#     Args:
#         player_positions (list): A list of player positions.
#         current_player (int): The index of the current player.
#         snakes (dict): Dictionary of snake positions (key: head, value: tail).
#         ladders (dict): Dictionary of ladder positions (key: base, value: top).
    
#     Returns:
#         list: Updated player positions after the turn.
#     """
    
#     roll = roll_dice()
#     print(f"Player {current_player + 1} rolled a {roll}")
    
#     new_position = player_positions[current_player] + roll
#     new_position = min(new_position, 100)  # Prevent going beyond 100
    
#     player_positions[current_player] = move_player(new_position, snakes, ladders)
    
#     print(f"Player {current_player + 1} moves to {player_positions[current_player]}")
#     return player_positions

# def play_game():

#      """
#     Runs the full game of Snakes and Ladders, alternating between two players.

#     The game continues until a player reaches position 100.
#     """
    
#     board_size = 100
#     snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
#     ladders = {4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
#     player_positions = create_players()

    
#      # Display ASCII Art at the start of the game
#     display_ascii_art("SNAKES AND LADDERS")  # Call the function from the utilities module to display ASCII art
#     # display_ascii_art_start_game()
    
#     print("Initial board with player starting positions:")
#     print_board_with_emojis(board_size, player_positions, snakes, ladders)
    
#     current_player = 0
#     while max(player_positions) < 100:
#         print(f"Player {current_player + 1}'s turn (Position: {player_positions[current_player]})")
#         user_input = input("Press Enter to roll the dice, or type 'q' to quit the game: ")
        
#         if user_input.lower() == 'q':
#             print("Exiting the game. Thanks for playing!")
#             break
        
#         player_positions = play_turn(player_positions, current_player, snakes, ladders)
        
#         print_board_with_emojis(board_size, player_positions, snakes, ladders)
        
#         if player_positions[current_player] == 100:
#             # Display ASCII Art at the end of the game
#             display_ascii_art()  # Call the function from the utilities module to display ASCII art
#             print(f"Player {current_player + 1} wins!")
#             break
        
#         current_player = 1 - current_player


def play_turn(player_positions, current_player, snakes, ladders):
    """
    Simulates a player's turn: rolling the dice, moving the player, and checking for snakes/ladders.
    
    Args:
        player_positions (list): A list of player positions.
        current_player (int): The index of the current player.
        snakes (dict): Dictionary of snake positions (key: head, value: tail).
        ladders (dict): Dictionary of ladder positions (key: base, value: top).
    
    Returns:
        list: Updated player positions after the turn.
    """
    roll = roll_dice()  # Simulate the dice roll
    print(f"Player {current_player + 1} rolled a {roll}")
    
    new_position = player_positions[current_player] + roll
    new_position = min(new_position, 100)  # Prevent moving beyond the last square
    
    # Move the player according to the dice roll and check for snakes or ladders
    player_positions[current_player] = move_player(new_position, snakes, ladders)
    
    print(f"Player {current_player + 1} moves to {player_positions[current_player]}")
    return player_positions


def play_game():
    """
    Runs the full game of Snakes and Ladders, alternating between two players.

    The game continues until a player reaches position 100.
    """
    board_size = 100
    # Snake and ladder positions on the board
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    # Initialize player positions with `create_players()`
    player_positions = create_players()

    # Display ASCII Art at the start of the game
    display_ascii_art("SNAKES AND LADDERS")  # Call the function from the utilities module to display ASCII art
    
    print("Initial board with player starting positions:")
    print_board_with_emojis(board_size, player_positions, snakes, ladders)
    
    current_player = 0  # Start with Player 1 (index 0)
    
    while max(player_positions) < 100:  # Game continues until a player reaches position 100
        print(f"Player {current_player + 1}'s turn (Position: {player_positions[current_player]})")
        user_input = input("Press Enter to roll the dice, or type 'q' to quit the game: ")
        
        if user_input.lower() == 'q':  # Allow the player to quit
            print("Exiting the game. Thanks for playing!")
            break
        
        player_positions = play_turn(player_positions, current_player, snakes, ladders)
        
        # Display updated board after the turn
        print_board_with_emojis(board_size, player_positions, snakes, ladders)
        
        if player_positions[current_player] == 100:  # Check if the current player wins
            # Display ASCII Art at the end of the game
            display_ascii_art("YOU WIN")  # Call the function from the utilities module to display ASCII art
            print(f"Player {current_player + 1} wins!")
            break
        
        # Switch to the other player
        current_player = 1 - current_player



