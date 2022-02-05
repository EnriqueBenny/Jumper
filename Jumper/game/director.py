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
        ob = Jumper.get_word()
        self._is_playing = True
        self._jumper = Jumper()
        self._player = Player()
        self._terminal_service = TerminalService()
        self._incorrect_guess = []
        self._user_input = ""
        self._first_letter = ob[0]
        self._second_letter = ob[1]
        self._third_letter = ob[2]
        self._fourth_letter = ob[3]
        self._fifth_letter = ob[4]
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
# The self._user_input arguement didn't exist, so I created it.
    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        self._user_input = input("Guess a letter [a-z] ")

#We are only using five letter words, so you can reduce the code here.
#The if statement in this method is empty, I added a pass to it so that the code wouldn't
#complain about being broken.
    def _do_updates(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        for i in range(0, len(self._jumper.word)):
            searching = self._jumper.word[i]
            if searching == self._user_input:
                #Set undercore index i equal to searching
                #It needs a list of underscores to loop through 
                pass

        # use terminal service to update the player after the guess for the do_outputs

#Do outputs still needs to be done, make sure to use the TerminalService
#class to do the outputs.        
    def _do_outputs(self):
        """
        Passes the text to be output to TerminalService
        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self, self._player)

        pass