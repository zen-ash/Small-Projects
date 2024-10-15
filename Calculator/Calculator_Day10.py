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


def calculator2():
    user_input = input("Enter :")
    lst1 = [0,1,2,3,4,5,6,7,8,9]
    for i in user_input:
        if i in icons:
        # if i=="+" or i=="-" or i =="*" or i=="/":
            operator_index = user_input.index(i)
            operator = user_input[operator_index]
    # print(operator_index)



    # for item in icons:
        # for i in user_input:
            # if item == i:
                # operator_index = user_input.index(i)
                # operator = user_input[operator_index]

    # print(operator)
    x = int(user_input[0:operator_index])
    # print(x)
    y= int(user_input[operator_index+1 : len(user_input)+1])
    # print(y)

    final_calc = icons[operator](x,y)
    print(final_calc)



calculator2()









# def calculator():
#     num1 = int(input("what is the first number: "))

#     while True:
#         print("Available Operators")
#         for item in icons:
#             print(item, end ="|")
#             # print(item)

#         action = input("pick an operator: ")

#         if action not in icons:
#                 print("Wrong Operator")
#                 continue
        
#         num2 = int(input("what is the next number: "))

#         result = icons[action](num1,num2)
#         print(f'result : {result}')

#         more_calc = input("Type 'y' to calculate more or 'n' to start a new calc.").lower()
#         if more_calc == "n":
#             os.system('cls')
#             # print("-"*30)
#             num1 = int(input("what is the first number: "))

#         elif more_calc == "y":
#             num1 = result


