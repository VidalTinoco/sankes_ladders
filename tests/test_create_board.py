import unittest
from snake_ladder.board.board_setup import create_board
from snake_ladder.snakes_ladders.check_interaction import move_player
from snake_ladder.utilities.roll_dice import roll_dice
from snake_ladder.board.display import print_board_with_emojis
from snake_ladder.players.player_setup import create_players
from snake_ladder.utilities.ascii_art import display_ascii_art


class TestCreateBoard(unittest.TestCase):

    def test_default_board_size(self):
        # Test the default board size (100)
        board = create_board()
        
        # The board should have exactly 100 squares
        self.assertEqual(len(board), 100)
        
        # All squares should be empty (⬜)
        self.assertTrue(all(square == '⬜' for square in board))
    
    def test_custom_board_size(self):
        # Test with a custom board size
        board_size = 64
        board = create_board(board_size)
        
        # The board should have exactly 64 squares
        self.assertEqual(len(board), board_size)
        
        # All squares should be empty (⬜)
        self.assertTrue(all(square == '⬜' for square in board))

