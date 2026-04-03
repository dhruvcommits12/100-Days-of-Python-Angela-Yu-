from art import logo

print(logo)
bidding_list={}
more_bidders="yes"

def find_highest_bidder(bidding_list):

    winner=""
    highest_bid=0

    for bidder in bidding_list:
        current_bid=bidding_list[bidder]
        if current_bid>highest_bid:
            highest_bid=current_bid
            winner=bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while more_bidders=="yes":
    
    name = input("What is your name: ")
    bid_price = int(input("What is your bid : $ "))
    bidding_list[name]=bid_price
    more_bidders = input("Are there any other bidders ? Type 'yes' or 'no'\n").lower()
    if more_bidders=="yes":
        print("\n"*28)

find_highest_bidder(bidding_list)



