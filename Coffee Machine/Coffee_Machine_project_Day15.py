coffee_info = {
    "espresso" :{
        "ingredients" : {
        "water" : 50,
        "coffee" : 18,
        "milk" : 0
    },
    "cost" : 1.5
    },

    "latte" : {
        "ingredients" : {
        "water" : 200,
        "coffee" : 24,
        "milk" : 150
    },
    "cost" : 2.5
    },
    "cappuccino" : {
    "ingredients" : {
        "water" : 250,
        "coffee" : 24,
        "milk" : 100
    },
    "cost": 3.0
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100 
}

def money_compare():
    print("please insert coins")
    user_quarters = int(input("How many quarters: "))
    user_dimes = int(input("How many dimes: ")) 
    user_nikles = int(input("How many nickles: "))
    user_penny = int(input("How many pennies: "))
    total_money = (user_quarters * .25) + (user_dimes *.10) + (user_nikles * .05) + (user_penny*.01)
    return total_money
    

def type_coffee(input):
    total_money = money_compare()
    if input == "espresso":
        if coffee_info["espresso"]["ingredients"]["water"] < resources["water"] and  coffee_info["espresso"]["ingredients"]["milk"] < resources["milk"] and coffee_info["espresso"]["ingredients"]["coffee"] < resources["coffee"] :
            if total_money >= coffee_info["espresso"]["cost"]:

                resources["coffee"] -= coffee_info["espresso"]["ingredients"]["coffee"]
                resources["milk"] -= coffee_info["espresso"]["ingredients"]["milk"]
                resources["water"] -= coffee_info["espresso"]["ingredients"]["water"]
                change = total_money - coffee_info["espresso"]["cost"]
                print(f"Your change is {change}")
                # print(resources)
            else:
                print("Not enough money")
        else:
            print("Not enought resources for espresso")
            return False

    elif input == "latte":
        if coffee_info["latte"]["ingredients"]["water"] < resources["water"] and  coffee_info["latte"]["ingredients"]["milk"] < resources["milk"] and coffee_info["latte"]["ingredients"]["coffee"] < resources["coffee"] :
            if total_money >= coffee_info["latte"]["cost"]:

                resources["coffee"] -= coffee_info["latte"]["ingredients"]["coffee"]
                resources["milk"] -= coffee_info["latte"]["ingredients"]["milk"]
                resources["water"] -= coffee_info["latte"]["ingredients"]["water"]
                change = total_money - coffee_info["latte"]["cost"]
                print(f"change is { change} ")
                # print(resources)
            else:
                print("Not enought money")
        else:
            print("Not enought resources for latte")
            return False

    elif input == "cappuccino":
        if coffee_info["cappuccino"]["ingredients"]["water"] < resources["water"] and  coffee_info["cappuccino"]["ingredients"]["milk"] < resources["milk"] and coffee_info["cappuccino"]["ingredients"]["coffee"] < resources["coffee"] :
            if total_money >= coffee_info["cappuccino"]["cost"]:

                resources["coffee"] -= coffee_info["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= coffee_info["cappuccino"]["ingredients"]["milk"]
                resources["water"] -= coffee_info["cappuccino"]["ingredients"]["water"]
                change = total_money - coffee_info["cappuccino"]["cost"]
                print(f"change is {change}")
                # print(resources)
            else:
                print("Not enought money")
        else:
            print("Not enought resources for cappuccino")
            return False



go_on = True

while go_on:
    user_input = input("What coffee do you want :  espresso | latte | cappucinno: ").lower()

    if user_input == "off":
        exit()
    if user_input == "report":
        print(resources)

    type_coffee(user_input)
    another_coffe = input("Want another coffee:").lower()
    if another_coffe == "no":
        go_on == False
