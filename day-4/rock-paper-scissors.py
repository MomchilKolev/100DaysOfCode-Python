import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice_str = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
)
choice_int = int(choice_str)

if choice_int not in [0, 1, 2]:
    print("Incorrect number choice")
    exit()

choices = [rock, paper, scissors]
choice = choices[choice_int]

print(f"{choice}\n")

computer_choice_int = random.randint(0, 2)
computer_choice = choices[computer_choice_int]
print("Computer chose:\n")
print(computer_choice)

if choice_int == 0:
    if computer_choice_int == 0:
        print("Draw\n")
    elif computer_choice_int == 1:
        print("You lose\n")
    else:
        print("You win\n")
elif choice_int == 1:
    if computer_choice_int == 1:
        print("Draw\n")
    elif computer_choice_int == 2:
        print("You lose\n")
    else:
        print("You win\n")
elif choice_int == 2:
    if computer_choice_int == 2:
        print("Draw\n")
    elif computer_choice_int == 0:
        print("You lose\n")
    else:
        print("You win\n")
exit()
