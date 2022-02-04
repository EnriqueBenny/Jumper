class Player:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Player.

        Args:
            self (player): An instance of player.
        """
        
        self._line1 =  '''
                     _____
                        '''
        self._line2 = '''
                    /_____\
        '''
        self._line3 = '''

                    \     / '''
        self._line4 = '''
                     \   /
        '''
        self._line5 = "0"
        self._line6 = '''
                      /|\
                      / \
                    '''
    
    def display_parachute(self):
        print(f'''
                {self._line1}
                {self._line2}
                {self._line3}
                {self._line3}''')
    
    def is_found(self):
        """Whether or not the letter has been found.

        Args:
            self (player): An instance of player.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return (self._distance[-1] == 0)
        
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)