from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
all_bids = []

def add_dictionary(name,price):
    bid_dictionary = {}
    bid_dictionary["name"] = name
    bid_dictionary["price"] = price
    all_bids.append(bid_dictionary)


bidding_finished = False

while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid?$"))
    add_dictionary(name,price)
    should_continue = input("Is there another person bidding?Type 'Yes' or 'No'.").lower()
    if should_continue == "no":
        bidding_finished = True
        clear()
        sleep(.2)
        

    elif should_continue == "yes":        
        clear()
        sleep(.2)

highest_bid = 0
for bid in all_bids:
    for val in bid:
        if bid["price"] > highest_bid:
            highest_bid = bid["price"]
            winner = bid["name"]
  
print(f"The winner is {winner} with a bid of {highest_bid}")