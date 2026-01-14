MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3
    }
}

def report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def refill(resources):
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("Machine refilled.")

def deposit():
    money = 0
    money += 0.25 * int(input("How many quarters?: "))
    money += 0.1 * int(input("How many dimes?: "))
    money += 0.05 * int(input("How many nickels?: "))
    money += 0.01 * int(input("How many pennies?: "))
    return money

def has_enough_resources(resources, ingredients):
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def pay(resources, price, money):
    if money < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    resources["money"] += price
    
    if money > price:
        print(f"Here is ${money - price:.2f} in change.")
    else:
        print("Thank you for paying")

    return True

def make_coffee(resources, coffee_type):
    for ingredient, amount in MENU[coffee_type]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {coffee_type} ☕ Enjoy!")

def coffee_machine(resources):
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    match coffee_type:
        case "report":
            report(resources)
        case "refill":
            refill(resources)
        case "espresso" | "latte" | "cappuccino":
            drink = MENU[coffee_type]
            if has_enough_resources(resources, drink["ingredients"]):
                money = deposit()
                if pay(resources, drink["cost"], money):
                    make_coffee(resources, coffee_type)
        case "off":
            return False
        case _:
            print("Invalid option. Please choose again.")
    return True

if __name__ == "__main__":
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }
    is_on = True
    while is_on:
        is_on = coffee_machine(resources)