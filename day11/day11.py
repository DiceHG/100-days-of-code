from logo import logo
from random import choices, choice

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
    hand.append(choice(list(deck)))
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    
while True:
    if input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ') == 'n':
        break
    
    print('\n' * 20)
    print(logo)

    player = choices(list(deck), k=2)
    dealer = choices(list(deck), k=2)


    while sum(player) < 21 and sum(dealer) != 21:
        print(f'Your cards: {player}, current score: {sum(player)}')
        print(f'Dealer\'s first card: {dealer[0]}')
        turn = input('Type \'y\' to get another card, type \'n\' to pass: ')

        if turn == 'y':
            deal_card(player)
        else:
            break

    while sum(dealer) < 16 and sum(player) < 21:
        deal_card(dealer)

    print(f'Your final hand: {player}, final score: {sum(player)}')
    print(f'Dealer\'s final hand: {dealer}, final score: {sum(dealer)}')

    if sum(player) == sum(dealer):
        print('It\'s a draw 🙃')
    elif sum(player) == 21 and len(player) == 2:
        print('Blackjack !! You win 🎉')
    elif sum(dealer) == 21 and len(player) == 2:
        print('What a shame, the dealer has a blackjack. You lose 😱')
    if sum(player) > 21:
        print('You went over. You lose 😭')
    elif sum(dealer) > 21:
        print('Dealer went over. You win 😁')
    elif sum(player) > sum(dealer):
        print('You win 😃')
    else:
        print('You lose 😤')
        