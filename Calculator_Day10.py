number = 0

def add(num1,num2):
    global number
    number = num1+num2
    return number

def subtract(num1,num2):
    global number
    number = num1-num2
    return number

def multiply(num1,num2):
    global number
    number = num1*num2
    return number

def divide(num1,num2):
    global number
    if num2 != 0:
        number = num1/num2
    else:
        print("Division by 0 error.")
        number= None
    return number

def icons():
    print(f'+\n-\n*\n/')


num1 = int(input("what is the first number: "))
go_on = True

while go_on:
    icons()
    action = input("pick an operator: ")
    num2 = int(input("what is the next number: "))

    if action == "+":
        add(num1,num2)

    elif action == "-":
        subtract(num1,num2)

    elif action == "*":
        multiply(num1,num2)

    elif action == "/":
        divide(num1,num2)

    else:
        print("Wrong Operator")
        continue

    if number is not None:
        print(f'The result is {number}')


    more_calc = input("Type 'y' to calculate more or 'n' to start a new calc.").lower()
    if more_calc == "n":

        num1 = int(input("what is the first number: "))

    elif more_calc == "y":
        num1 = number



