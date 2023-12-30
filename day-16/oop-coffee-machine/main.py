from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def run():
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        return
    if choice == "report":
        coffee_maker.report()
        return run()

    drink = menu.find_drink(choice)
    if drink is None:
        print("Impossible drink choice. Try again.")
        return run()

    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
    return run()


run()
