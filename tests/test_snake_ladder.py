import unittest
from unittest.mock import patch
from snake_ladder.snakes_ladders.check_interaction import move_player
from snake_ladder.utilities.roll_dice import roll_dice
from snake_ladder.board.display import print_board_with_emojis
from snake_ladder.players.player_setup import create_players
from snake_ladder.utilities.ascii_art import display_ascii_art

class TestSnakesAndLadders(unittest.TestCase):

    def test_move_player_snake(self):
        # Testing when a player lands on a snake
        snakes = {16: 6, 47: 26}
        ladders = {4: 14, 9: 31}
        position = 16
        with patch('builtins.print') as mocked_print:
            new_position = move_player(position, snakes, ladders)
            self.assertEqual(new_position, 6)  # Player should go to snake tail (6)
            mocked_print.assert_called_with("Player slides down the snake from 16 to 6")

    def test_move_player_ladder(self):
        # Testing when a player lands on a ladder
        snakes = {16: 6, 47: 26}
        ladders = {4: 14, 9: 31}
        position = 4
        with patch('builtins.print') as mocked_print:
            new_position = move_player(position, snakes, ladders)
            self.assertEqual(new_position, 14)  # Player should go to ladder top (14)
            mocked_print.assert_called_with("Player climbs the ladder from 4 to 14")
    
    def test_move_player_no_snake_or_ladder(self):
        # Testing when a player lands on a square with no snake or ladder
        snakes = {16: 6, 47: 26}
        ladders = {4: 14, 9: 31}
        position = 10
        with patch('builtins.print') as mocked_print:
            new_position = move_player(position, snakes, ladders)
            self.assertEqual(new_position, 10)  # Player's position remains the same
            mocked_print.assert_not_called()  # No print statement should be called

