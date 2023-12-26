import art
import random
import os

print(art.logo)

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, secret_number, attempts):
    """Check answer and return number of turns remaining"""
    attempts -= 1
    if guess == secret_number:
        print(f"You got it! The number was {secret_number}")
    elif guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print("Too low.")
    if attempts == 0:
        print("Better luck next time 😀")
    return attempts

def play():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randrange(101)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = HARD_TURNS if difficulty == 'hard' else EASY_TURNS
    guess = 0

    while attempts > 0 and guess != secret_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, secret_number, attempts)

play()
while input("Play again? 'y' or 'n': ") == 'y':
    os.system('clear')
    play()
        
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

