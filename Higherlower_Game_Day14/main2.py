import random
from data import data_insta


def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account["country"]
    return f'{account_name}, {account_descr}, {account_country}'


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
go_on =True
while go_on:
        
    account_a = random.choice(data_insta)
    account_b = random.choice(data_insta)
    if account_a == account_b:
        account_b = random.choice(data_insta)

    print(f"Compare A : {format_data(account_a)}")
    print("Vs")
    print(f"Compare B : {format_data(account_b)}")


    guess = input("Which one is bigger 'A' or 'B': ").lower()


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right. Your score is {score}")
        account_a = account_b
        account_b = {}
        print(f'account a is {account_a}')

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        go_on = False



