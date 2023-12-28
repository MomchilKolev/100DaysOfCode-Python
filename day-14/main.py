# Print logo
import random
import os
import art
import game_data


def format_data(account):
    """Format the account data and return it"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."


def correct_guess(guess, a_followers, b_followers):
    """Check if guess is correct and return True or False"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    score = 0
    end = False
    participant_a = random.choice(game_data.data)
    participant_b = random.choice(game_data.data)
    print(art.logo)
    while not end:
        # Handle 2 identical choices
        while participant_b["name"] == participant_a["name"]:
            participant_b = random.choice(game_data.data)

        print(f"Compare A: {format_data(participant_a)}")
        print(art.vs)
        print(f"Against B: {format_data(participant_b)}.")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        os.system("clear")

        if correct_guess(choice, participant_a["follower_count"], participant_b["follower_count"]):
            score += 1
            print(art.logo)
            print(f"You're right! Current score: {score} 🔥")
            participant_a = participant_b
            participant_b = random.choice(game_data.data)
        else:
            end = True

    print(f"Sorry, that's wrong. Final score: {score}")


play_game()
while input("Play again? 'Y' or 'N': ").lower() == "y":
    play_game()

# Show battle
# - choose participant 1
# - choose participant 2
# Ask for input
# Show correct
# If correct
# - increase score
# - show next battle
# - - participant 2 becomes new participant 1
# Else
# - show score
# - ask if try again
