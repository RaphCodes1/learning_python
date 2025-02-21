from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("welcome to Coffee Machine!")
while 1:
    type = input("What wold you like? (" + menu.get_items() + "):")
    if type == "report":
        coffee_maker.report()
        money_machine.report()
    elif type == "off":
        break
    else:
        drink = menu.find_drink(type)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                cost = drink.cost
                if money_machine.make_payment(cost):
                    coffee_maker.make_coffee(drink)
print("Thanks for using coffee machine")