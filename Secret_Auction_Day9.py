# SILENT AUCTION
import os
auct_dict = {}

max_bid = 0

go_on = True
while go_on:

    bidder_name = input("Enter the bidder name: ")
    bid_ammount = int(input("Enter your bid: "))

    auct_dict[bidder_name] = bid_ammount

    if bid_ammount > max_bid:
        max_bid =bid_ammount

    for item in auct_dict:
        if auct_dict[item] == max_bid:
            max_bidder = item

    more_bidders = input("Do you have anyone else to bid: ").lower()
    if more_bidders == "yes":
        os.system('cls')
    if more_bidders == "no" :
        go_on = False


# print(auct_dict)
print(f'{max_bidder} won and the highest bid is {max_bid}.')