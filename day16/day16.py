from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffee_machine():
    button = input(f"What would you like? ({menu.get_items()}): ")

    if button == 'off':
        return False
    elif button == "report":
        coffee_maker.report()
        money_machine.report()
    elif button == "espresso" or button == "latte" or button == "cappuccino":
        drink = menu.find_drink(button)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Invalid option. Please choose again.")
    return True

if __name__ == "__main__":
    is_on = True
    while is_on:
        is_on = coffee_machine()