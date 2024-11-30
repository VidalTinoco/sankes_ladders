import unittest
from snake_ladder.board.board_setup import create_board


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

