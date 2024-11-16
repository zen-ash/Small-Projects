from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = 
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user_input = input("What do you want (espresso/latte/cappuccino/): ").lower()



if user_input == "off":
    exit

if user_input == "report":
    coffee_maker.report()