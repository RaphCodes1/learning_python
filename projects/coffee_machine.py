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
    "money": 0
}

end = 0

def print_resource(resource):
    print("Water: " + str(resource["water"]) + "ml")
    print("Milk: " + str(resource["milk"]) + "ml")
    print("Coffee: " + str(resource["coffee"]) + "g")
    if resource["money"]:
        print("Money: $" + str(resource["money"]))

def add_coins(menu, resources, balance, drink):
    total = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    balance.append(0.25 * quarters)
    balance.append(0.10 * dimes)
    balance.append(0.05 * nickels)
    balance.append(0.01 * pennies)
    for i in range(0, 3):
        total += balance[i]
    print(f"Money given: {round(total,2)}")
    if total >= menu[drink]["cost"]:
        change = round(total - menu[drink]["cost"],2)
        print("here is your change: $" + str(change))
        resources["money"] += menu[drink]["cost"]
        return 1
    else:
        print("Sorry that's not enough money. Money Refunded")
        return 0

def check_available(menu, resources, drink):
    if drink == "espresso":
        check_ingredients = [resources["water"] - menu[drink]["ingredients"]["water"],
                             resources["coffee"] - menu[drink]["ingredients"]["coffee"]]
        for i in range(0, 1):
            if check_ingredients[i] < 0:
                if i == 0:
                    print(f"Sorry there is not enough water")
                elif i == 1:
                    print(f"Sorry there is not enough coffee")
                return 0
    else:
        check_ingredients = [resources["water"] - menu[drink]["ingredients"]["water"],
                             resources["coffee"] - menu[drink]["ingredients"]["coffee"],
                             resources["milk"] - menu[drink]["ingredients"]["milk"]]
        for i in range(0,2):
            if check_ingredients[i] < 0:
                if i == 0:
                    print(f"Sorry there is not enough water")
                elif i == 1:
                    print(f"Sorry there is not enough coffee")
                elif i == 2:
                    print(f"Sorry there is not enough milk")
                return 0
    return 1

def refill_resource(resources):
    refill_water = int(input("Refill Water: "))
    resources["water"] += refill_water
    refill_milk = int(input("Refill Milk: "))
    resources["milk"] += refill_milk
    refill_coffee = int(input("Refill Coffee: "))
    resources["coffee"] += refill_coffee

def make_drink(menu, resources, drink):

    if not drink == "espresso":
        resources["milk"] -= menu[drink]["ingredients"]["milk"]
    resources["water"] -= menu[drink]["ingredients"]["water"]
    resources["coffee"] -= menu[drink]["ingredients"]["coffee"]
    print(f"Here is your {drink}. Enjoy!.")

print("Welcome to coffee machine!")
while end == 0:
    balance = []
    user_in = input("What wold you like? (espresso/latte/cappuccino): ")
    if user_in == "off":
        end = 1
    elif user_in == "report":
        print_resource(resources)
    elif user_in == "refill":
        refill_resource(resources)
    elif user_in == "espresso":
        if check_available(MENU, resources, "espresso"):
            if add_coins(MENU, resources, balance, "espresso"):
                make_drink(MENU, resources, "espresso")
    elif user_in == "latte":
        if check_available(MENU, resources, "latte"):
            if add_coins(MENU, resources, balance, "latte"):
                make_drink(MENU, resources, "latte")
    elif user_in == "cappuccino":
        if check_available(MENU, resources, "cappuccino"):
            if add_coins(MENU, resources, balance, "cappuccino"):
                make_drink(MENU, resources, "cappuccino")
