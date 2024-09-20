# SILENT AUCTION
import os
auct_dict = {}

max_bid = 0
max_bidder = ''

def auction(bidder_name, bid_ammount):
    global max_bid, max_bidder
    auct_dict[bidder_name] = bid_ammount
    if bid_ammount > max_bid:
        max_bid =bid_ammount
        max_bidder = bidder_name

def clear_screen(more_bidders):
    if more_bidders == "yes":
        os.system('cls')



go_on = True
while go_on:
    name_of_bidder = input("Enter the bidder name: ")
    ammount_bid = int(input("Enter your bid: "))
    auction(name_of_bidder,ammount_bid)

    num_of_bidder = input("Do you have anyone else to bid: ").lower()
    clear_screen(num_of_bidder)

    if num_of_bidder == "no":
        go_on = False

print(f'{max_bidder} won and the highest bid is ${max_bid}.')
