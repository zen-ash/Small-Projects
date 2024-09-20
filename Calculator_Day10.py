import os

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        print("Division by 0 error.")
        return None
    
icons = {
    "+" : add, "-": subtract, "*" : multiply, "/":divide
}

def calculator():
    num1 = int(input("what is the first number: "))
    # go_on = True

    while True:
        print("Available Operators")
        for item in icons:
            print(item)

        action = input("pick an operator: ")

        if action not in icons:
                print("Wrong Operator")
                continue
        
        num2 = int(input("what is the next number: "))

        result = icons[action](num1,num2)


        print(f'result : {result}')

        more_calc = input("Type 'y' to calculate more or 'n' to start a new calc.").lower()
        if more_calc == "n":
            os.system('cls')
            num1 = int(input("what is the first number: "))

        elif more_calc == "y":
            num1 = result


calculator()


# import os

# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     if num2 != 0:
#         return num1 / num2
#     else:
#         print("Division by 0 error.")
#         return None

# icons = {
#     "+" : add, "-": subtract, "*" : multiply, "/": divide
# }

# # def clear_screen():
# #     # Check platform and use the appropriate command
# #     if os.name == 'nt':  # For Windows
# #         os.system('cls')
# #     else:  # For macOS and Linux
# #         os.system('clear')

# def calculator():
#     num1 = int(input("What is the first number: "))

#     while True:
#         print("Available Operators")
#         for item in icons:
#             print(item)

#         action = input("Pick an operator: ")

#         if action not in icons:
#             print("Wrong Operator")
#             continue

#         num2 = int(input("What is the next number: "))

#         result = icons[action](num1, num2)

#         print(f'Result: {result}')

#         more_calc = input("Type 'y' to calculate more or 'n' to start a new calculation: ").lower()
#         if more_calc == "n":
#             # clear_screen()  # Call the function to clear the screen
#             num1 = int(input("What is the first number: "))
#         elif more_calc == "y":
#             num1 = result

# calculator()
