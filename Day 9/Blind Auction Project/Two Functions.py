# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
# TODO-5: Use functions!

print("\n" * 100)
from art import logo

print(logo)
print("Welcome to the secret auction program!")

bids = {}  # Initialize empty dict


def intake(bids):
    """Collect one bidder's info and add to bids. Returns True if more bidders, False if done."""
    name = input("What is your name?: ")
    price = int(input("How much would you like to bid?: $"))
    bids[name] = price
    question = input("Is there anyone else?\nType 'yes' or 'no'\n").lower()
    print("\n" * 100)
    if question == "no":
        return False  # No more bidders
    else:
        return True  # Continue collecting


def find_highest_bidder(bidding_dictionary):
    """Find and announce the highest bidder."""
    if not bidding_dictionary:  # Edge case: no bids
        print("No bids were placed!")
        return

    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder  # Update winner here

    print(f"The winner is {winner} with a bid of ${highest_bid}!")


# Main loop: Collect bids until done
more_bidders = True
while more_bidders:
    more_bidders = intake(bids)

# Calculate and announce winner
find_highest_bidder(bids)


# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
# TODO-5: Use functions!
#
# print("\n" * 100)
# from art import logo
# print(logo)
# print("Welcome to the secret auction program!")
# ready_to_calc = False
# bids = {}
#
# def intake(name, price):
#     name = input("What is your name?: ")
#     price = int(input("How much would you like to bid?: $"))
#     bids[name] = price
#     question = input("Is there anyone else?,\nType 'yes' or 'no'\n").lower()
#     print("\n" * 100)
#     if question == "no":
#         ready_to_calc = True
#         find_highest_bidder(bids)
#
#
#
# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     winner = ""
#     for key in bids:
#         if bids[key] > highest_bid:
#             highest_bid = bids[key]
#     for bidder in bids:
#         if bids[bidder] == highest_bid:
#             print(f"The winner is {bidder} with a bid of {highest_bid}!")
#
# while ready_to_calc == False:
#     intake(name=, price=)