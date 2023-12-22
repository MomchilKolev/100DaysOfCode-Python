from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    output_text = ""
    for letter in text:
        position = alphabet.index(letter) if letter in alphabet else -1
        if position < 0:
            output_text += letter
        else:
            new_position = position + shift if direction == 'encode' else position - shift
            output_text += alphabet[new_position]
    print(f"The {direction}d text is {output_text}")

print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift < 0 or shift > 25:
        shift = int(input("Type a shift number between 1 and 25: "))
    caeser(text, shift, direction)

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    result = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if result == 'no':
        should_continue = False
        print("Goodbye")