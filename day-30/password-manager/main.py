# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
from tkinter import *
from tkinter import messagebox

# import pyperclip

from password_generator import generate_password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    """Save Password Entry to File"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not validate_entries(website, email, password):
        return
    print("AFTER validation")

    try:
        with open("data.json", mode="r") as file:
            # Get data
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            # Save new data
            json.dump(new_data, file, indent=4)
    else:
        # Update data
        data.update(new_data)

        with open("data.json", mode="w") as file:
            # Save updated data
            json.dump(data, file, indent=4)
    finally:
        reset_entries()


def validate_entries(*args):
    """Check if any entry is empty and return False, else True"""
    for entry in args:
        if entry == "":
            messagebox.showinfo(title="Oops", message="Please don't leave any entries empty.")
            return False
    return True


def reset_entries():
    """Reset website and password entries"""
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def generate_password_entry():
    """Generate and populate a new password"""
    new_password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    # pyperclip.copy(new_password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="You need to store a password before you can "
                                                   "search your password manager")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            password_entry.delete(0, END)
            password_entry.insert(0, password)
            messagebox.showinfo(
                title="Credentials found",
                message=f"Website {website}\nYour email {email}\nYour Password {password}"
            )
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Password Manager")
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)
email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "a@b.c")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate Password", command=generate_password_entry)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=40, command=save_to_file)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
