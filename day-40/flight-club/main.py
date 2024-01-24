import polars
import polars as pl
from polars.exceptions import NoDataError

print("Welcome to the Flight Potato Club.")
print("We find the best deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Type your email again.\n")

if '' in [first_name, last_name, email, confirm_email]:
    print("Inputs cannot be empty.")

if email != confirm_email:
    print("Emails must match.")

try:
    df = pl.read_csv("users.csv")

except FileNotFoundError:
    print("Create file")
    df = pl.DataFrame()
    with open("users.csv", "w") as data_file:
        pass
except NoDataError:
    print("Empty CSV file")
    df = pl.DataFrame()
finally:
    new_row = pl.DataFrame({"First Name": first_name, "Last Name": last_name, "Email": email})
    result  = pl.concat([df, new_row])
    result.write_csv("users.csv")

    print("Success! Your email has been added. Look forward to amazing deals.")
