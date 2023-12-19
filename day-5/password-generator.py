# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total = number_of_letters + number_of_symbols + number_of_numbers
password = ""
password_list = []

# Pick letters
if number_of_letters > 0:
    for n in range(0, number_of_letters):
        password_list += random.choice(letters)
# Pick symbols
if number_of_symbols > 0:
    for n in range(0, number_of_symbols):
        password_list += random.choice(symbols)
# Pick numbers
if number_of_numbers > 0:
    for n in range(0, number_of_numbers):
        password_list += random.choice(numbers)

# characters = [*chosen_letters, *chosen_symbols, *chosen_numbers]

# # Choose random character
# # Append to password
# for n in range(0, total):
#   next = random.randint(0, len(characters) - 1)
#   password += characters.pop(next)

random.shuffle(password_list)
password = "".join(password_list)

print(f"Here is your password: {password}")
