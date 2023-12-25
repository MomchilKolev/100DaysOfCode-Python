from art import logo
import random
import os

print(logo)

def draw_card():
    """Pure function to draw a random card and return it"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards."""
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        print("Blackjack! You win!")
        return 0 # Blackjack
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def compare(player_score, computer_score):
    """Compare player score and computer score to decide winner"""
    if player_score == computer_score:
        return "Draw 😐"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 🤯 "
    elif player_score == 0:
        return "Win with Blackjack 🔥 "
    elif player_score > 21:
        return "You went over, you lose 😢"
    elif computer_score > 21:
        return "Opponent went over, You win 😮"
    elif player_score > computer_score:
        return "You win 😎"
    else:
        return "You lose 😤"

def blackjack():
    game_over = False

    player_cards = [draw_card(), draw_card()]
    computer_cards = [draw_card(), draw_card()]
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    while not game_over:
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if player_score > 21 or player_score == 0 or computer_score == 0:
            game_over = True
        else:
            player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_should_deal == 'y':
                player_cards.append(draw_card())
                player_score = calculate_score(player_cards)
            else:
                game_over = True

    while computer_score < 17 and not computer_score == 0:
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    print(f"{compare(player_score, computer_score)}")

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    os.system('clear')
    blackjack()