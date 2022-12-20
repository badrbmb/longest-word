# pylint: disable=too-few-public-methods

"""
Contains class definitions to play the game
"""

import random
import string
import requests

class Game:
    """Create a game instance"""

    URL = "https://wagon-dictionary.herokuapp.com/"

    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_letters) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Check if a given world is valid"""
        if not isinstance(word, str):
            return False
        # check if the given  world is a subset of the desired solution
        if not all(x in self.grid for x in list(word)):
            return False
        # check if the given world is real word
        response = requests.get(f"{URL}/{word}")
        # make sure status code is 200
        response.raise_for_status()
        # get reponse
        return response.json()['found']
