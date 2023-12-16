# 26. Day 2 Project: Tip Calculator
print("Welcome to the tip calculator.")

# Get inputs
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# Calculate
total_with_tip = bill * (1 + tip_percent / 100)
bill_per_person = round(total_with_tip / number_of_people, 2)  # 13.6, should be 13.60
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")