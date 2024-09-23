import random
import os
print("welcom to Number Guessing Game")


# def num_to_guess():
#     num_to_guess = random.randint(1,100)
#     print(num_to_guess)
#     return num_to_guess

def guess(num_to_guess, attempt):
    go_on = True
    while go_on:
        guess_input = int(input("Enter your guess : "))
        if guess_input == num_to_guess:
            print("Correct. You WIN")
            print("*" * 5)
            break
        elif guess_input > num_to_guess:
            print("Too high")
            attempt -=1
        else:
            print("Too low")
            attempt -=1
            
        print(f'You have {attempt} attempts left.')
        if attempt == 0:
            print("You lose")
            print("*" * 5)
            go_on = False
 

def main():
    play_again = True
    while play_again:
        # num_to_guess()
        num_to_guess = random.randint(1,100)
        # print(num_to_guess)
        difficulty = input("Type 'easy' for easy mode and 'hard' for hard mode: ").lower()
        if difficulty == "easy":
            attempt = 10
        if difficulty == "hard":
            attempt = 5
        guess(num_to_guess, attempt)

        wanna_play_again = input(f"Want to play again 'yes or no': ").lower()
        if wanna_play_again != "no":
            os.system('cls')
        else:
            play_again = False
            

main()