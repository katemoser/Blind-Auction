from replit import clear
import art
import for_sale
import random
#HINT: You can call clear() to clear the output in the console.

bids = {}

def add_bid(name, bid):
    bids[name] = bid

def find_winner():
    winner = ""
    winning_bid = 0
    for bidder in bids:
        if bids[bidder] > winning_bid:
            winning_bid = bids[bidder]
            winner = bidder
    print(f"The winner of the {item_for_sale} auction is {winner}, with ${winning_bid}. Congratulations!")

auction_over = False

print(art.logo)
item_for_sale = for_sale.items[random.randint(0,len(for_sale.items)-1)]

print(f"Welcome to the Silent Auction! Today's item for sale:\n\n{item_for_sale}\n")


while not auction_over:
    user_name = input("What is your name?\n")
    user_bid = int(input("What is your bid (USD)?\n$"))
    add_bid(user_name, user_bid)
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if continue_bidding == "no":
        auction_over = True
    clear()
find_winner()
