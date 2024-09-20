import os
# number = 0

def add(num1,num2):
    global number
    return num1+num2

def subtract(num1,num2):
    global number
    return num1-num2

def multiply(num1,num2):
    global number
    return num1*num2

def divide(num1,num2):
    global number
    if num2 != 0:
        return num1/num2
    else:
        print("Division by 0 error.")
        return None

# def icons():
#     print(f'+\n-\n*\n/')

icons = {
    "+" : add, "-": subtract, "*" : multiply, "/":divide
}

def calculator():
    num1 = int(input("what is the first number: "))
    go_on = True

    while go_on:
        # icons()
        print("Available Operators")
        for item in icons:
            print(item)

        action = input("pick an operator: ")

        if action not in icons:
                print("Wrong Operator")
                continue
        
        num2 = int(input("what is the next number: "))


        # for item in icons:
        #     if action == item:
        #         operation = icons[item]
        #     else:
        #         print("Wrong Operator")
        #         continue

        result = icons[action](num1,num2)

        # if action == "+":
        #     add(num1,num2)

        # elif action == "-":
        #     subtract(num1,num2)

        # elif action == "*":
        #     multiply(num1,num2)

        # elif action == "/":
        #     divide(num1,num2)

        # else:
        #     print("Wrong Operator")
        #     continue

        # if number is not None:
        #     print(f'The result is {number}')

        print(f'result : {result}')


        more_calc = input("Type 'y' to calculate more or 'n' to start a new calc.").lower()
        if more_calc == "n":
            os.system('cls')
            num1 = int(input("what is the first number: "))


        elif more_calc == "y":
            num1 = result

calculator()