
    # display_board = ['⬜' for _ in range(board_size)]
    
    # for snake_start in snakes:
    #     display_board[snake_start - 1] = '🐍'
    # for ladder_start in ladders:
    #     display_board[ladder_start - 1] = '🪜'
    
    # for i, pos in enumerate(player_positions):
    #     if player_positions[0] == player_positions[1]:
    #         display_board[player_positions[0] - 1] = '🔴'
    #         break
    #     elif pos <= board_size:
    #         display_board[pos - 1] = '🔵' if i == 0 else '🟡'

    # print("-" * 85)  # Print horizontal line between rows

    
    # for i in range(9, -1, -1):
    #     start = i * 10
    #     end = start + 10
    #     row = display_board[start:end]
    #     if i % 2 == 1:
    #         row = row[::-1]
    #     formatted_row = ["{:^4}".format(x) for x in row]
    #     #print(" | ".join(formatted_row))
    #     print("| " + " | ".join(formatted_row)+ "|")
    #     if i >= 0:
    #         print("-" * 80)  # Print horizontal line between rows
    # print("\n")


def print_board_with_emojis(board_size, player_positions, snakes, ladders):
    
    """
    Prints the Snakes and Ladders game board with emojis to represent the state of the game.

    Parameters:
    board_size (int): The total number of squares on the board (typically 100 for a 10x10 grid).
    player_positions (list): A list containing the current positions of the players on the board. 
                              The list should have two elements representing the positions of Player 1 and Player 2.
    snakes (dict): A dictionary where the keys are the starting positions of snakes, and the values are the corresponding ending positions.
    ladders (dict): A dictionary where the keys are the starting positions of ladders, and the values are the corresponding ending positions.

    The board is displayed as a 10x10 grid where:
    - '⬜' represents an empty space.
    - '🐍' represents a snake.
    - '🪜' represents a ladder.
    - '🔵' represents Player 1.
    - '🟡' represents Player 2.
    - '🔴' represents both players on the same square (if applicable).
    
    The grid is displayed from top to bottom, with the bottom-most row having the highest numbered squares.
    Odd-numbered rows are reversed to simulate a back-and-forth movement across the board.
    
    Example:
    If the game has 2 players at positions 1 and 5, with a snake at position 16 and a ladder at position 4,
    the board will be displayed with Player 1 at position 1 and Player 2 at position 5, 
    the snake at position 16, and the ladder at position 4.
    """
    
    # FUNCTION 1
    # Initialize the display board with empty squares
    display_board = ['⬜' for _ in range(board_size)]
    
    # FUNCTION 2
    # Place snakes on the board
    for snake_start in snakes:
        display_board[snake_start - 1] = '🐍'
    
    # FUNCTION 3
    # Place ladders on the board
    for ladder_start in ladders:
        display_board[ladder_start - 1] = '🪜'
    
    # FUNCTION 4
    # Place players on the board
    for i, pos in enumerate(player_positions):
        if pos <= board_size:
            # Check if both players are on the same position
            if player_positions[0] == player_positions[1]:
                display_board[pos - 1] = '🔴'  # Indicate same position with a red circle
            else:
                # Assign player 1 (🔵) and player 2 (🟡) to their respective positions
                display_board[pos - 1] = '🔵' if i == 0 else '🟡'

    print("-" * 80)  # Print horizontal line between rows

    # FUNCTION 5
    # Print the board row by row, alternating row directions
    for i in range(9, -1, -1):  # Loop through rows 9 to 0
        start = i * 10
        end = start + 10
        row = display_board[start:end]
        
        # Reverse the row if the row index is odd
        if i % 2 == 1:
            row = row[::-1]
        
        # Format each element of the row to center the emojis within a 4-character width
        formatted_row = ["{:^4}".format(x) for x in row]
        
        # Print the formatted row
        print(" | ".join(formatted_row))
        
        # Print a horizontal line after each row except the last one
        if i >= 0:
            print("-" * 80)
    
    print("\n")
