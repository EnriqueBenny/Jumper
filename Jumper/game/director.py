from game.terminal_service import TerminalService
from game.player import Player
from game.jumper import Jumper


class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    """

    def __init__(self):
        """Constructs a new Director.
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._jumper = Jumper()
        self._player = Player()
        self._terminal_service = TerminalService()
        self._incorrect_guess = []
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        self.user_input = input("Guess a letter [a-z] ")
        
    def _do_updates(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        for i in range(0, len(self._jumper.word)):
            serching = self._jumper.word[i]
            if serching == self.user_input:
                #Set undercore index i equal to searching
                #It needs a list of underscores to loop through 

        
    def _do_outputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        