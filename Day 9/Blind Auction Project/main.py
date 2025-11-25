# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
# TODO-5: Use functions!

print("\n" * 100)
from art import logo
print(logo)
print("Welcome to the secret auction program!")
ready_to_calc = False
bidding_dictionary = {}


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
            print(f"The winner is {bidder} with a bid of {highest_bid}!")
def greet(name, price):
    bidding_dictionary[name] = price
    question = input("Is there anyone else?,\nType 'yes' or 'no'\n").lower()
    print("\n" * 100)
    if question == "no":
        ready_to_calc = True
        find_highest_bidder(bidding_dictionary)

while ready_to_calc == False:
    name = input("What is your name?: ")
    price = int(input("How much would you like to bid?: $"))
    greet(name, price)








