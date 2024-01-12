# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
#import pyperclip


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    """Save Password Entry to File"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not validate_entries(website, email, password):
        return

    is_okay = messagebox.askokcancel(title=website, message=f"There are the details entered: "
                                                            f"\nEmail: "
                                                            f"{email} \nPassword: {password}\nIs it okey to save?")
    if is_okay:
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")

        reset_entries()


def validate_entries(*args):
    """Check if any entry is empty and return False, else True"""
    for entry in args:
        if entry == "":
            messagebox.showinfo(title="Oops", message="Please don't leave any entries empty.")
            return False
        else:
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
    #pyperclip.copy(new_password)


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
website_entry = Entry(width=43)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "a@b.c")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password_entry)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=40, command=save_to_file)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
