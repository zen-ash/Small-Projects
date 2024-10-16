# from data import coffee_info
# from data import resources
# from data import profit
from data import *

def money_compare():
    "Return the total money "
    print("please insert coins")
    user_quarters = int(input("How many quarters: "))
    user_dimes = int(input("How many dimes: ")) 
    user_nikles = int(input("How many nickles: "))
    user_penny = int(input("How many pennies: "))
    total_money = (user_quarters * .25) + (user_dimes *.10) + (user_nikles * .05) + (user_penny*.01)
    return total_money
    
def is_resource_sufficient(order_ingredients):
    "Retunr True if ingredients available , return False if not"
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
        
def transaction(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Your change is : {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money")
        return False
    
def make_coffee(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print("Here's your coffee enjoy!😊")


go_on = True

while go_on:
        
    user_input = input("What coffee do you want :  espresso | latte | cappuccino: ").lower()

    if user_input == "off":
        go_on = False

    elif user_input == "report":
        for i in resources:
            print(f"{i} : {resources[i]} ")
        print(f'Money : {profit}')

    else:
        drink = coffee_info[user_input]
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = money_compare()
                if transaction(payment, drink["cost"]):
                    make_coffee(drink["ingredients"])
        else:
            print("Sorry, we don't serve that.")