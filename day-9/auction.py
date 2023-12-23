import art
import os

print(art.logo)
print("Welcome to the secret auction program!")

def find_highest_bidder(bids):
    highest_bid = 0
    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
    os.system('clear')
    print(f"The winner is {name} with a bid of ${bids[name]}.")

bids = {}
more_bidders = True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if bidders == 'no':
        more_bidders = False
        find_highest_bidder(bids)
    else:
        os.system('clear')