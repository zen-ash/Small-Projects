import random
import os


list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10,10]


def add_card(user_cards, comp_cards):
    for i in range(2):
        user_cards.append(random.choice(list_of_cards))
        comp_cards.append(random.choice(list_of_cards))

    print(f"Your cards are : {user_cards}")
    # print(f' Comp cards are : {comp_cards}')
    print(f' Comp cards are : {comp_cards[:-1]}')

def more_cards(user_cards, comp_cards):
    more_cards_need = True
    while more_cards_need:
        user_more_cards = input("Enter 'y' to get more cards and 'n' to pass: ").lower()

        if user_more_cards == 'y':           
            user_cards.append(random.choice(list_of_cards))
            comp_cards.append(random.choice(list_of_cards))
            

            user_sum = sum(user_cards)
            comp_sum = sum(comp_cards)

            if user_sum > 21 and 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_sum = sum(user_cards)

            print(f"User cards: {user_cards},Computer Cards:  {comp_cards}")

            if user_sum > 21:
                more_cards_need = False
            elif comp_sum > 21:
                more_cards_need = False
                
 
        elif user_more_cards == 'n':
            comp_sum = sum(comp_cards)
            while comp_sum < 17:
                comp_cards.append(random.choice(list_of_cards))
                comp_sum = sum(comp_cards)
            print(f'Comp Sum is less than 17. comp has got another card : {comp_cards[:-1]}')    
            more_cards_need = False

    
def calculate_scores(user_cards, comp_cards):
    user_sum = sum(user_cards)
    comp_sum = sum(comp_cards)
    if user_sum > 21:
        print(f"You lose. You sum is {user_sum} and is over 21.")
    elif comp_sum > 21:
        print(f"Comp lose. Comp sum is {comp_sum} and is over 21.")
    elif user_sum == comp_sum:
        print("Its a tie...")
    elif user_sum > comp_sum:
        print(f"You won. your sum is {user_sum} anc comp sum is {comp_sum}")
    else:
        print(f"You lose. your sum is {user_sum} anc comp sum is {comp_sum}")
    

def main():
    go_on = True
    while go_on:
        user_cards = []
        comp_cards = []
        add_card(user_cards, comp_cards)
        more_cards(user_cards, comp_cards)
        calculate_scores(user_cards, comp_cards)
        play_again = input("Wanna play again: 'yes' or 'no' ").lower()
        if play_again == "no":
            go_on = False
        else:
            os.system('cls')
     

main()