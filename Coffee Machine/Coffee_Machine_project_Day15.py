
from data import coffee_info
from data import resources
from data import profit


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
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        return True
        
def transaction(payment, drink_cost):
    if payment >= drink_cost:
        change = payment - drink_cost
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
    return resources[item]



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

        
            








# def type_coffee(input):
#     total_money = money_compare()
#     if input == "espresso":
#         if coffee_info["espresso"]["ingredients"]["water"] < resources["water"] and  coffee_info["espresso"]["ingredients"]["milk"] < resources["milk"] and coffee_info["espresso"]["ingredients"]["coffee"] < resources["coffee"] :
#             if total_money >= coffee_info["espresso"]["cost"]:

#                 resources["coffee"] -= coffee_info["espresso"]["ingredients"]["coffee"]
#                 resources["milk"] -= coffee_info["espresso"]["ingredients"]["milk"]
#                 resources["water"] -= coffee_info["espresso"]["ingredients"]["water"]
#                 change = total_money - coffee_info["espresso"]["cost"]
#                 print(f"Your change is {change}")
#                 # print(resources)
#             else:
#                 print("Not enough money")
#         else:
#             print("Not enought resources for espresso")
#             return False

#     elif input == "latte":
#         if coffee_info["latte"]["ingredients"]["water"] < resources["water"] and  coffee_info["latte"]["ingredients"]["milk"] < resources["milk"] and coffee_info["latte"]["ingredients"]["coffee"] < resources["coffee"] :
#             if total_money >= coffee_info["latte"]["cost"]:

#                 resources["coffee"] -= coffee_info["latte"]["ingredients"]["coffee"]
#                 resources["milk"] -= coffee_info["latte"]["ingredients"]["milk"]
#                 resources["water"] -= coffee_info["latte"]["ingredients"]["water"]
#                 change = total_money - coffee_info["latte"]["cost"]
#                 print(f"change is { change} ")
#                 # print(resources)
#             else:
#                 print("Not enought money")
#         else:
#             print("Not enought resources for latte")
#             return False

#     elif input == "cappuccino":
#         if coffee_info["cappuccino"]["ingredients"]["water"] < resources["water"] and  coffee_info["cappuccino"]["ingredients"]["milk"] < resources["milk"] and coffee_info["cappuccino"]["ingredients"]["coffee"] < resources["coffee"] :
#             if total_money >= coffee_info["cappuccino"]["cost"]:

#                 resources["coffee"] -= coffee_info["cappuccino"]["ingredients"]["coffee"]
#                 resources["milk"] -= coffee_info["cappuccino"]["ingredients"]["milk"]
#                 resources["water"] -= coffee_info["cappuccino"]["ingredients"]["water"]
#                 change = total_money - coffee_info["cappuccino"]["cost"]
#                 print(f"change is {change}")
#                 # print(resources)
#             else:
#                 print("Not enought money")
#         else:
#             print("Not enought resources for cappuccino")
#             return False



# go_on = True

# while go_on:
#     user_input = input("What coffee do you want :  espresso | latte | cappucinno: ").lower()

#     if user_input == "off":
#         exit()
#     if user_input == "report":
#         print(resources)

#     type_coffee(user_input)
#     another_coffe = input("Want another coffee:").lower()
#     if another_coffe == "no":
#         go_on == False
