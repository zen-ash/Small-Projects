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

# print(coffee_info)
# print("_____________________")
# print(coffee_info["espresso"]["ingrideints"]["water"])



def type_coffee(input):
    if input == "espresso":
        if coffee_info["espresso"]["ingredients"]["water"] < resources["water"] and  coffee_info["espresso"]["ingredients"]["milk"] < resources["milk"] and coffee_info["espresso"]["ingredients"]["coffee"] < resources["coffee"] :
            resources["coffee"] -= coffee_info["espresso"]["ingredients"]["coffee"]
            resources["milk"] -= coffee_info["espresso"]["ingredients"]["milk"]
            resources["water"] -= coffee_info["espresso"]["ingredients"]["water"]
            print(resources)
        else:
            print("Not enought resources for espresso")
            return False

    elif input == "latte":
        if coffee_info["latte"]["ingredients"]["water"] < resources["water"] and  coffee_info["latte"]["ingredients"]["milk"] < resources["milk"] and coffee_info["latte"]["ingredients"]["coffee"] < resources["coffee"] :
            resources["coffee"] -= coffee_info["latte"]["ingredients"]["coffee"]
            resources["milk"] -= coffee_info["latte"]["ingredients"]["milk"]
            resources["water"] -= coffee_info["latte"]["ingredients"]["water"]
            print(resources)
        else:
            print("Not enought resources for latte")
            return False

    elif input == "cappuccino":
        if coffee_info["cappuccino"]["ingredients"]["water"] < resources["water"] and  coffee_info["cappuccino"]["ingredients"]["milk"] < resources["milk"] and coffee_info["cappuccino"]["ingredients"]["coffee"] < resources["coffee"] :
            resources["coffee"] -= coffee_info["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= coffee_info["cappuccino"]["ingredients"]["milk"]
            resources["water"] -= coffee_info["cappuccino"]["ingredients"]["water"]
            print(resources)
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
