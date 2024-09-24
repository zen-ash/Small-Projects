import random
import os
from data import data_insta

A = []
B = []
score = 0
keep_playing = True


def random_index():
    return random.randint(0, len(data_insta)-1)

def details(lst):
    index = random_index()
    name = data_insta[index]["name"]
    follower = data_insta[index]["follower_count"]
    descr = data_insta[index]["description"]
    country = data_insta[index]["country"]
    lst.extend([name, follower, descr, country])
    return follower


def compare(follower_1, follower_2):
    global score
    global keep_playing
    user_guess = input("who has more followers 'A' or 'B': ").lower()
    if user_guess == 'a':
        if follower_1 > follower_2:
            score += 1
            print("Correct")
        else:
            print("You lose")
            keep_playing = False
    
    elif user_guess == 'b':
        if follower_2 > follower_1:
            score += 1
            print("Correct")
        else:
            print("You lose")
            keep_playing = False
            
    print(f"Score is {score}")


def main():
    go_on = True
    man_a = details(A)
    man_b = details(B)
    if man_a == man_b:
        B.clear()
        man_b = details(B)
    else:
        pass

    while go_on:
        global keep_playing
        keep_playing = True
        while keep_playing:
            

            print(f"A : {A[0]}, {A[2]}, {A[3]}, ")
            print(f"B : {B[0]}, {B[2]}, {B[3]}, ")

            compare(A[1], B[1])
            A.clear()
            for i in B:
                A.append(i)
            B.clear()
            man_b = details(B)

        wanna_play_again = input("Wanna play again 'yes' or 'no': ").lower()
        if wanna_play_again != "yes":
            go_on = False
            os.system('cls')
        

main()
