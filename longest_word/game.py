# pylint: disable=too-few-public-methods

"""
Contains class definitions to play the game
"""

import random
import string



class Game:
    """Create a game instance"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_letters) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Check if a given world is valid"""
        if not isinstance(word, str):
            return False
        return all(x in self.grid for x in list(word))
