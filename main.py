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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient_ingredients(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] > resources[item]:
            print(f"sorry insufficient {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(total, cost_drink):
    if total >= cost_drink:
        change = total - cost_drink
        print(f"your change:{change}")
        global profit
        profit = profit + cost_drink
        return True
    else:
        print(f"sorry insufficient cash,your money {total} is refunded")
        return False


def make_coffee(drink_name, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
profit = 0
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"Money:${profit}")
    elif choice == "off":
        is_on = False
    else:
        drink = MENU[choice]
        ordered_ingredients = drink["ingredients"]
        if is_sufficient_ingredients(ordered_ingredients):
            total = process_coins()
            if is_transaction_successful(total, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
