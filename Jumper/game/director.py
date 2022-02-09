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
        # Interacts with TerminalService
        self._terminal_service = TerminalService()
        # Determines victory
        self._victory = False
        # Tracks the correct guesses 
        self._progress_tracking = []
        self._word_list = list(self._jumper.word)
        # Tracks the incorrect guesses
        self._incorrect_guess = []
        # Takes the user inputs to be processed
        self._user_input = ""
        self._letter = ""
        
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        # Outputs to Terminal
        self._terminal_service.write_text(self._player.guess_word)
        print('\n')
        for i in self._visual:
            print(i)
        # Runs Game loop
        while self._is_playing:
            # Clear screen each iteration cross platform (Note: doesnt let me start the game with displaying the visual)
            #os.system('cls' if os.name=='nt' else 'clear')
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    # This method will get the input from the user.
    def _get_inputs(self):
        """
        Gets the inputs from the player to be sent to other methods to determine validity.
        Args:
            self (Director): An instance of Director.
        """
        # Gets the player's inputs
        self._user_input = input("\rGuess a letter [a-z]: ")
        self._letter = self._user_input
        # Will check if user enter just a letters only.
        if self._letter.isdigit() == True:
            print("You entered a digit, please enter a character only!\n")
            Director._get_inputs(self)

    def _do_updates(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        #Sends the guess and the word into the is_found method in the Player Class
        guess = self._player.is_found(self._jumper.word, self._user_input)
        # Puts the incorrect guesses in a list to display to the player.
        if guess == False:
            self._visual.pop(0)
            self._incorrect_guess.append(self._letter) 
        else: 
            guess
            self._progress_tracking.append(self._user_input)
        #If the game is lost, this will replace the jumper's head with an 'x'
        if len(self._visual) == 3:
            self._visual.insert(0,"    X")
            self._is_playing = False
            Player._defeat_screen(self)
        # If this statement is true, then the player wins the game.
        self._victory = Player.win_condition(self, self._word_list, self._progress_tracking)
            
      
    def _do_outputs(self):
        """
        Passes the text to be output to TerminalService
        Args:
            self (Director): An instance of Director.
        """
        # Prints the current state of the guesses.
        self._terminal_service.write_text(self._player.guess_word)
        print('\n')
        for i in self._visual:
            print(i)
        # Prints the incorrect guesses.
        print(f"incorrect guesses: {str(self._incorrect_guess)[1:-1]}")
        #Displays the victory tkinter screen
        if self._victory == True:
            Player._victory_screen(self)
            self._is_playing = False
            
        
      
