import unittest
from snake_ladder.snakes_ladders.check_interaction import move_player
from snake_ladder.utilities.roll_dice import roll_dice
from snake_ladder.board.display import print_board_with_emojis
from snake_ladder.players.player_setup import create_players
from snake_ladder.utilities.ascii_art import display_ascii_art
from io import StringIO
import sys


class TestPrintBoardWithEmojis(unittest.TestCase):

    def setUp(self):
        # Setting up any necessary test data
        self.board_size = 100
        self.snakes = [16, 47, 49]  # Example snake positions
        self.ladders = [3, 22, 31]  # Example ladder positions
        self.player_positions = [1, 10]  # Example player positions

    def test_initial_empty_board(self):
        # Capture the output of the function
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_board_with_emojis(self.board_size, self.player_positions, self.snakes, self.ladders)
        
        # Checking if the board contains emojis in the expected positions
        output = captured_output.getvalue()
        
        # Check if the snake emoji is placed at the correct positions
        self.assertIn('🐍', output)
        
        # Check if the ladder emoji is placed at the correct positions
        self.assertIn('🪜', output)
        
        # Check if player 1 (🔵) and player 2 (🟡) are placed in the correct positions
        self.assertIn('🔵', output)
        self.assertIn('🟡', output)
        
        # Check that the board has the expected size (10x10 grid)
        self.assertEqual(output.count('⬜'), 100 - len(self.snakes) - len(self.ladders) - 2)  # 100 squares minus snakes, ladders, and players
        
    def test_players_on_same_square(self):
        # Move both players to the same position
        self.player_positions = [10, 10]
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_board_with_emojis(self.board_size, self.player_positions, self.snakes, self.ladders)
        
        output = captured_output.getvalue()
        
        # Check if both players are on the same position (red circle)
        self.assertIn('🔴', output)
        self.assertNotIn('🔵', output)
        self.assertNotIn('🟡', output)
        
    def test_empty_board(self):
        # Test with no snakes, ladders, or players
        self.player_positions = [1, 1]
        self.snakes = []
        self.ladders = []
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_board_with_emojis(self.board_size, self.player_positions, self.snakes, self.ladders)
        
        output = captured_output.getvalue()
        
        # Check if the board is completely empty except for the player positions
        self.assertIn('⬜', output)
        self.assertEqual(output.count('⬜'), 98)  # Only two player positions should be different
    
    def tearDown(self):
        # Reset standard output
        sys.stdout = sys.__stdout__
