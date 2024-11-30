import art  # Import the art package


#def display_ascii_art():
   # """Displays the Snake and Ladder ASCII art at the start of the game."""
   #print(art.text2art("SNAKES AND LADDERS"))  # Display the ASCII art for "Snake and Ladder"

def display_ascii_art(text=None):

    """
    Displays ASCII art based on the provided text.

    This function uses the 'art' package to generate and print ASCII art for specific messages. 
    If the provided text matches "SNAKES AND LADDERS", the art for that message is shown. 
    For any other input (or no input), the default message "CONGRATULATIONS" is displayed as ASCII art.

    Parameters:
        text (str, optional): The string to display as ASCII art. If "SNAKES AND LADDERS", a special 
                               game-related art is shown. Otherwise, a default "CONGRATULATIONS" art is shown.
                               If no text is provided, the default art is displayed.

    Example:
        display_ascii_art("SNAKES AND LADDERS") 
        # Outputs the "SNAKES AND LADDERS" ASCII art.
        
        display_ascii_art() 
        # Outputs the "CONGRATULATIONS" ASCII art by default.
    """
    if text == "SNAKES AND LADDERS":
        print(art.text2art("SNAKES AND LADDERS"))
    else:
        print(art.text2art("CONGRATULATIONS"))  # Default message for unmatched text