import random

class Jumper:
    """The Person with their life on the line, the purpose of the game is
    to guess the word the jumper is thinking of before the player runs out of 
    guesses and kills the jumper.
        word (str): The word the jumper is thinking of, guessing this correctly ends the
        game.
    """

    def __init__(self):
        """Constructs a new Jumper.
        Args:
            self (Jumper): An instance of Jumper.
        """
        self._word = ""
        
    def get_word(self):
        """Gets the current jumper's word.
        Returns:
            word: The current word.
        """
        word_pool = ["fuzzy", "abide", "about", "abyss", "carve", "heart", "brain",
        "alice", "actor", "zebra", "yummy", "youth", "youse", "magic"]
        guess = random.choice(word_pool)
        self._word = guess
        return self._word
        
    # def move_location(self, location):
    #     """Sends out the current word as a guess.
    #     Args:
    #         self (Seeker): An instance of Jumper.
    #         guess (str): The given word.
    #     """
    #     word_guess = self._word
    #     return word_guess