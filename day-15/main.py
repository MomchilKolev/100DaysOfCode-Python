# Program Requirements
## Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
## Turn off the Coffee Machine by entering “off” to the prompt
## Print report
## Check resources sufficient
## Process coins
## Check transaction successful
## Make Coffee
## Deduct resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def sufficient_resources(drink):
    """Check if there are sufficient resources for the chosen drink, return True or False"""
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def deduct_resources(drink):
    """For a given drink deduct the resources it cost"""
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]


def handle_transaction(drink):
    """Handle transaction, make necessary changes to resources"""
    coins_provided = 0
    coins_required = drink["cost"]

    print(f"Please insert coins - ${drink['cost']}.")

    for coin in coins:
        if coins_provided >= coins_required:
            continue
        number_of_coins = int(input(f"how many {coin}?: "))
        coins_provided += coins[coin] * number_of_coins

    if coins_provided < coins_required:
        print("Sorry that's not enough money. Money refunded.")
        return False

    # Successful transaction
    change = round(coins_provided - coins_required, 2)
    ## Add money
    resources["money"] += coins_required
    ## Deduct resources
    deduct_resources(drink)

    print(f"Here is ${change} in change.")
    return True


def report():
    """Print resources report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def run():
    """A recursive function to run the program after each selection process end, unless "off" is specified as choice"""
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Base case
    if choice == "off":
        return

    # Recursive case
    if choice == "report":
        report()
        return run()

    # Incorrect choice
    if choice not in MENU:
        print("In practice it's impossoble to choose an unavailable option.")
        return run()

    drink = MENU[choice]
    if not sufficient_resources(drink):
        return run()

    if handle_transaction(drink):
        print(f"Here is your {choice} ☕. Enjoy!")
    run()


run()
