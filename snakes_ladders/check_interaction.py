def move_player(position, snakes, ladders):

    """
    Moves the player based on their current position, considering the effects of snakes and ladders.

    If the player lands on a snake, they slide down to the snake's tail. If the player lands on a ladder,
    they climb up to the top. If the player is not on a snake or ladder, their position remains unchanged.

    Parameters:
    position (int): The current position of the player on the board (between 1 and 100).
    snakes (dict): A dictionary where the keys are the starting positions of snakes, and the values are the corresponding ending positions.
    ladders (dict): A dictionary where the keys are the starting positions of ladders, and the values are the corresponding ending positions.

    Returns:
    int: The new position of the player after considering any snakes or ladders. If the player is not on a snake or ladder, the original position is returned.
    
    Example:
    If the player is on position 16 and there is a snake at position 16 (with the tail at position 6), the function
    will return 6 and print "Player slides down the snake from 16 to 6".
    If the player is on position 4 and there is a ladder at position 4 (with the top at position 14), the function
    will return 14 and print "Player climbs the ladder from 4 to 14".
    """
    
    if position in snakes:
        print(f"Player slides down the snake from {position} to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Player climbs the ladder from {position} to {ladders[position]}")
        return ladders[position]
    return position


# Getter and Setter for snakes and ladders
#def get_snakes():
    """
    Returns the current dictionary of snakes (starting position -> ending position).
    """
#    return snakes

#def set_snakes(new_snakes):
    """
    Sets the new dictionary of snakes.
    
    Parameters:
    new_snakes (dict): A dictionary of snakes with the starting position as keys and the ending position as values.
    """
#    global snakes
#    snakes = new_snakes

#def get_ladders():
    """
    Returns the current dictionary of ladders (starting position -> ending position).
    """
#    return ladders

#def set_ladders(new_ladders):
    """
    Sets the new dictionary of ladders.
    
    Parameters:
    new_ladders (dict): A dictionary of ladders with the starting position as keys and the ending position as values.
    """
#    global ladders
#    ladders = new_ladders

#def generate_snakes_and_ladders(board_size=100, num_snakes=5, num_ladders=5):
    """
    Generates random positions for snakes and ladders on the board.

    This method randomly selects positions for both snakes and ladders ensuring:
    - The start position of a snake is greater than the end position (snake slide).
    - The start position of a ladder is less than the end position (ladder climb).
    
    Parameters:
    board_size (int): The total number of squares on the board (default is 100).
    num_snakes (int): The number of snakes to generate (default is 5).
    num_ladders (int): The number of ladders to generate (default is 5).

    Returns:
    dict, dict: Two dictionaries representing the generated snakes and ladders.
    """
#   new_snakes = {}
#    new_ladders = {}

    # while len(new_snakes) < num_snakes:
    #     start = random.randint(1, board_size - 1)
    #     end = random.randint(1, start - 1)  # Snake goes down, so end < start
    #     if start not in new_snakes and start not in new_ladders and end > 0:
    #         new_snakes[start] = end
    
    # while len(new_ladders) < num_ladders:
    #     start = random.randint(1, board_size - 1)
    #     end = random.randint(start + 1, board_size)  # Ladder goes up, so end > start
    #     if start not in new_ladders and start not in new_snakes:
    #         new_ladders[start] = end

    # return new_snakes, new_ladders


#def move_player(position, snakes, ladders):
    """
    Moves the player based on their current position, considering the effects of snakes and ladders.

    If the player lands on a snake, they slide down to the snake's tail. If the player lands on a ladder,
    they climb up to the top. If the player is not on a snake or ladder, their position remains unchanged.

    Parameters:
    position (int): The current position of the player on the board (between 1 and 100).
    snakes (dict): A dictionary where the keys are the starting positions of snakes, and the values are the corresponding ending positions.
    ladders (dict): A dictionary where the keys are the starting positions of ladders, and the values are the corresponding ending positions.

    Returns:
    int: The new position of the player after considering any snakes or ladders. If the player is not on a snake or ladder, the original position is returned.
    
    Example:
    If the player is on position 16 and there is a snake at position 16 (with the tail at position 6), the function
    will return 6 and print "Player slides down the snake from 16 to 6".
    If the player is on position 4 and there is a ladder at position 4 (with the top at position 14), the function
    will return 14 and print "Player climbs the ladder from 4 to 14".
    """
    # if position in snakes:
    #     print(f"Player slides down the snake from {position} to {snakes[position]}")
    #     return snakes[position]
    # elif position in ladders:
    #     print(f"Player climbs the ladder from {position} to {ladders[position]}")
    #     return ladders[position]
    # return position