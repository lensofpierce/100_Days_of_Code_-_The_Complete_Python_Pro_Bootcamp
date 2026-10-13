from art import logo
print(logo)

new_bidder = True
bidder_log = {}

def find_highest_bidder(bidder_dictionary):
    highest_bid = 0
    bid_leader = ""

    max(bidder_dictionary)

    for bidder in bidder_dictionary:
        bid_amount = bidder_log[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bid_leader = bidder
        else:
            continue
    print(f"The winner is {bid_leader} with a bid of ${highest_bid}.")

while new_bidder:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    bidder_log[name] = bid

    # TODO-3: Whether if new bids need to be added
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if add_bidder == 'no':
        new_bidder = False
        # TODO-4: Compare bids in dictionary
        find_highest_bidder(bidder_log)
    else:
        print("\n" * 100)





