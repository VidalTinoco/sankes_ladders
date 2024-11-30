import random

def roll_dice():

    """
    Simulates the rolling of a six-sided dice.

    This function generates a random integer between 1 and 6 (inclusive), representing a standard dice roll.

    Returns:
        int: A random number between 1 and 6, inclusive, simulating a dice roll.

    Example:
        roll = roll_dice()
        print(roll)  # Outputs a random number between 1 and 6, like 4 or 2.
    """
    return random.randint(1, 6)