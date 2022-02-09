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
        self.word = ""
        
    def get_word(self):
        """Gets the current jumper's word.
        Returns:
            word: The current word.
        """
        #The List of Words the game will use.
        word_pool = ["layer", "abide", "about", "doubt", "carve", "heart", "brain",
        "alice", "actor", "zebra", "draft", "youth", "youse", "magic"]
        guess = random.choice(word_pool)
        self.word = guess
        return self.word
