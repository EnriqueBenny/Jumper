from ctypes import alignment
import tkinter as tk
from tkinter import *
class Player:
    """The person guessing the hidden word to keep the jumper from dying. 
    The responsibility of player is to keep track of its parachute. 
    Attributes:
        _(parachute): the parachute used in the game to represent the Jumper.
        
    """

    def __init__(self):
        """Constructs a new Player.
        Args:
            self (player): An instance of player.
        """
        
    def display_parachute(self):
        """ Displays the parachute in the game that represents the Jumper.
        Args:
            self (player): An instance of player.
            Returns (obj): parachute
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
            boolean: True if the letter was found; false if otherwise.
        """
        is_found = False
        for i, letter in enumerate(jumper_word):
            if letter == jumper_guess:
                self.guess_word[i] = letter
                is_found = True
        return is_found

    def win_condition(self, word_list, guess_list):
        """Whether or not the words match up, determines if the win condition has been met.
        This is done by incrementing a counter for each correct letter.
        Args: 
            self (player): An instance of player.
        Returns:
            boolean: True if they match, False if they don't.
        """
        # If the count reaches the same number as the len() of the word_list, condition will be
        # returned as True, meaning the player wins the game.
        count = 0
        condition = False
        for i in word_list:
            if i in guess_list:
                count += 1
            else:
                pass
        if count == len(word_list):
            condition = True
        return condition

    def _victory_screen(self):
        """
        If the game is won and the player is saved, this method will run
        and display the player's victory.
        Args:
            self (tkinter): an instance of tkinter.
        """
        root = tk.Tk()
        T = tk.Label(root, text="You Saved the Jumper!", height=5, width=25, font=("Arial", 60), fg="gold", bg="blue")
        T.pack()
        T.after(3000, lambda:root.destroy())
        tk.mainloop()
    
    def _defeat_screen(self):
        """
        If the game is lost and the player dies, this method will run
        and display the player's defeat.
        Args:
            self (tkinter): an instance of tkinter.
        """
        root = tk.Tk()
        T = tk.Label(root, text="Your Jumper Died!", height=5, width=25, font=("Arial", 60), fg="red", bg="black")
        T.pack()
        T.after(3000, lambda:root.destroy())
        tk.mainloop()

