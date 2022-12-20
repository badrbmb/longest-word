from longest_word.game import Game
import string

# tests/test_game.py
class TestGame:
    def test_game_initialization(self):
            # setup
            game = Game()
            # exercise
            grid = game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            assert any([t in string.ascii_uppercase for t in grid])

    def test_is_valid(self):

            test_grid = list('DSREOOVEJSUSOLF')
            # setup
            game = Game()
            # exercise
            game.grid = test_grid
            # verifiy
            test_word = 'OVERDOSE'
            assert game.is_valid(test_word) is True

    def test_is_not_valid(self):

        test_grid = list('ETIAGDNNERNIEGABLOBL')
        # setup
        game = Game()
        # exercise
        game.grid = test_grid
        # verifiy
        test_word = 'POETRY'
        assert game.is_valid(test_word) is False


    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
