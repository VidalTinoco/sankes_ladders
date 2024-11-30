import unittest
from unittest.mock import patch
from snake_ladder.snakes_ladders.check_interaction import move_player
from snake_ladder.utilities.roll_dice import roll_dice
from snake_ladder.board.display import print_board_with_emojis
from snake_ladder.players.player_setup import create_players
from snake_ladder.utilities.ascii_art import display_ascii_art


class TestSnakesAndLadders(unittest.TestCase):

    # Test the roll_dice function
    def test_roll_dice(self):
        for _ in range(100):  # Roll the dice 100 times to check for correctness
            roll = roll_dice()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

    # Test the move_player function with snakes and ladders
    def test_move_player_snakes(self):
        # Test if the player correctly moves to the tail of a snake
        snakes = {16: 6, 47: 26, 49: 11}
        ladders = {4: 14, 9: 31}
        
        # Player at position 16 should move to 6 due to the snake
        self.assertEqual(move_player(16, snakes, ladders), 6)
        
        # Player at position 49 should move to 11 due to the snake
        self.assertEqual(move_player(49, snakes, ladders), 11)

    def test_move_player_ladders(self):
        # Test if the player correctly moves to the top of a ladder
        snakes = {16: 6, 47: 26, 49: 11}
        ladders = {4: 14, 9: 31}

        # Player at position 4 should move to 14 due to the ladder
        self.assertEqual(move_player(4, snakes, ladders), 14)

    # Test the play_turn function
    @patch('builtins.input', return_value='')  # Mock the input for user interaction
    def test_play_turn(self):
        # Player 1 starts at position 1
        player_positions = [1, 1]
        current_player = 0
        snakes = {16: 6, 47: 26, 49: 11}
        ladders = {4: 14, 9: 31}
        
        # Simulate the player's turn
        new_player_positions = play_turn(player_positions, current_player, snakes, ladders)
        
        # Check if the player has moved correctly
        self.assertGreater(new_player_positions[current_player], player_positions[current_player])
    
    # Test the play_game function (simplified version)
    @patch('builtins.input', return_value='')  # Mock the input for user interaction
    def test_play_game(self):
        # For the sake of testing, we'll only check that the game progresses
        board_size = 100
        snakes = {16: 6, 47: 26, 49: 11}
        ladders = {4: 14, 9: 31}
        
        # Initialize player positions
        player_positions = create_players()
        
        # Start the game with a player on position 1
        current_player = 0
        player_positions[current_player] = 1
        
        # Simulate one turn and check if the player position updates
        player_positions = play_turn(player_positions, current_player, snakes, ladders)
        
        # Check that player position has updated (i.e., it has moved forward)
        self.assertGreater(player_positions[current_player], 1)
        
        # Simulate a few more turns to see if the game progresses
        for _ in range(10):
            player_positions = play_turn(player_positions, current_player, snakes, ladders)
            self.assertGreater(player_positions[current_player], 1)

    # Test the create_players function (player initialization)
    def test_create_players(self):
        # Ensure that the players start at position 1
        player_positions = create_players()
        self.assertEqual(player_positions, [1, 1])

    # Test the print_board_with_emojis function
    @patch('builtins.print')  # Mock the print function to capture output
    def test_print_board_with_emojis(self, mock_print):
        board_size = 100
        player_positions = [1, 1]
        snakes = {16: 6, 47: 26}
        ladders = {4: 14, 9: 31}
        
        # Print the initial board state
        print_board_with_emojis(board_size, player_positions, snakes, ladders)
        
        # Check that the function calls print
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()
