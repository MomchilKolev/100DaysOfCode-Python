# TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()
    
with open("Input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()

# for each name in invited_names.txt
for name in names:
    # Replace the [name] placeholder with the actual name.
    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as new_letter:
        new_letter_text = starting_letter.replace("[name]", name.strip())
        # Save the letters in the folder "ReadyToSend".
        new_letter.write(new_letter_text)
