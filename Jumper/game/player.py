class Player:
    """The person falling with a parachute. 
    
    The responsibility of player is to keep track of its parachute. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Player.

        Args:
            self (player): An instance of player.
        """
        # we need the _ _ _ _ _ as a line 0 that prints out as well. but this one has to be editable so maybe use terminal service
        # or make it an text string from director?
        
        
    
    def display_parachute(self):
        """Args:
            self (player): An instance of player.
            """
        line1 = '  _____'
        line2 = ' /_____\\'
        line3 = ' \\     / '
        line4 = '  \\   /'
        line5 = "    0"
        line6 = '   /|\\'
        line7 = '   / \\ \n'
        line8 = '^^^^^^^^^'
        parachute = [line1,line2,line3,line4,line5,line6,line7,line8]
        
        return parachute
    
    def is_found(self, jumper_word, jumper_guess):
        """Whether or not the letter has been found.

        Args:
            self (player): An instance of player.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        is_found = False
        for i, letter in enumerate(jumper_word):
            if letter == jumper_guess:
                self.guess_word[i] = letter
                is_found = True
        
        return is_found
        
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)