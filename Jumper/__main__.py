#What is this re, and why is it importing A?
from re import A
from game.director import Director

director = Director()
director.start_game()

"""
Jumper is just hangman, we need five letter words, 
we're going to make this our own by displaying the incorrect guesses.
"""