import pandas

from game import Game

states = pandas.read_csv("50_states.csv")
game = Game()

# Use a loop to allow the user to keep guessing
while len(game.guessed_states) < 50:
    game.ask()
