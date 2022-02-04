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
        self._life = 4
    
    def get_hint(self):
        """Gets a hint for the seeker.

        Args:
            self (player): An instance of player.
        Returns:
            string: A hint for the player.
        """
        hint = "(-.-) Nap time."
        if self._life[-1] == 0:
            hint = "(;.;) You found me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint

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