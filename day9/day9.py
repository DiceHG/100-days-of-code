bidders = {}

while True:
    name = input('What is your name?\n')
    bid = int(input('How much is your bid?\n'))

    bidders[name] = bid

    if input('Are there more users? Type \'yes\' or \'no\'\n') == 'no':
        break

highest_bidder = None
highest_bid = 0

for bidder, bid in bidders.items():
    if highest_bid < bid:
        highest_bid = bid
        highest_bidder = bidder

print(highest_bidder)
