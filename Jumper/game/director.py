import os
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
        self._jumper.word = Jumper.get_word(self)
        self._player = Player()
        self._visual = Player.display_parachute(self)
        # Setup word that contains user's guesses
        self._player.guess_word = ['_'] * len(self._jumper.word)
        self._terminal_service = TerminalService()
        self._incorrect_guess = []
        self._user_input = ""
        self._letter = ""
        
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service.write_text(self._player.guess_word)
        print('\n')
        for i in self._visual:
            print(i)
        
        while self._is_playing:
            # Clear screen each iteration cross platform (Note: doesnt let me start the game with displaying the visual)
            #os.system('cls' if os.name=='nt' else 'clear')
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
# The self._user_input arguement didn't exist, so I created it.
    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        self._user_input = input("\rGuess a letter [a-z]: ")
        self._letter = self._user_input

        while self._letter.isdigit() == True:
            print("You entered a digit, please enter a character only")
            break       

#The if statement in this method is empty, I added a pass to it so that the code wouldn't
#complain about being broken.
    def _do_updates(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        guess = self._player.is_found(self._jumper.word, self._user_input)
        if guess == False:
            self._visual.pop(0)
            self._incorrect_guess.append(self._letter) 
        else: 
            guess
        if len(self._visual) == 3:
            self._visual.insert(0,"    X")
            self._is_playing = False

        # use terminal service to update the player after the guess for the do_outputs

#Do outputs still needs to be done, make sure to use the TerminalService
#class to do the outputs.        
    def _do_outputs(self):
        """
        Passes the text to be output to TerminalService
        Args:
            self (Director): An instance of Director.
        """


        self._terminal_service.write_text(self._player.guess_word)
        print('\n')
        for i in self._visual:
            print(i)
        print(f"incorrect guesses: {str(self._incorrect_guess)[1:-1]}")
        pass     
            
        
      