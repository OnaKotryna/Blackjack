from presentation import display_cards, display_output, display_card, display_card_art, clear_view
import dealer

DECK = [
    '1♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    '1♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '1♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    '1♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
]

end_cases = {
    "bust": "It's a bust",
    "player": "You Won. Congrats",
    "draw": "Pretty dissapointing, it's a draw..",
    "blackjack": "BLACKJACK",
    "dealer": "You Lost. lol",
}


def play():
    """Game flow"""
    # start game
    player_hand, dealer_hand, deck = start()
    display_cards('player', player_hand)
    display_card("dealer", dealer_hand[0])
    if dealer.get_hand_value(player_hand) < 21:
        # check if player wants to take card
        hit_or_stand(player_hand, dealer_hand, deck)
    # end game
    end(player_hand, dealer_hand, deck)


def start():
    """Initiates game: cleans view and returns dealt cards"""
    clear_view()
    display_card_art()
    deck = DECK
    return get_game_hands(deck)


def get_game_hands(deck):
    """Deals Cards"""
    player_hand, deck = dealer.get_hand(deck)
    dealer_hand, deck = dealer.get_hand(deck)
    return player_hand, dealer_hand, deck


def hit_or_stand(player_hand, dealer_hand, deck):
    """Checks if player wants to hit or stand"""
    while True:
        next_card = input("Hit? y/n\n").lower()
        # clear view
        clear_view()
        display_card_art()

        if next_card.startswith('n'):
            break
        elif next_card.startswith('y'):
            #  deals card for players
            player_hand, deck = dealer.hit(player_hand, deck)
            # check if not exceeded 21
            if dealer.get_hand_value(player_hand) >= 21:
                break
            display_card("player", player_hand[-1])
            display_cards('player', player_hand)
            # displays a dealers first card
            display_card("dealer", dealer_hand[0])


def end(player_hand, dealer_hand, deck):
    """Displays game outcome"""
    winner = get_winner(player_hand, dealer_hand, deck)
    display_cards('player', player_hand)
    display_cards('dealer', dealer_hand)
    display_output(end_cases[winner])


def get_winner(player_hand, dealer_hand, deck):
    player_hand_value = dealer.get_hand_value(player_hand)
    if player_hand_value > 21:
        return "bust"

    dealer_hand_value = dealer.get_hand_value(dealer_hand)
    while dealer_hand_value < 17:
        dealer_hand, deck = dealer.hit(dealer_hand, deck)
        dealer_hand_value = dealer.get_hand_value(dealer_hand)

    if player_hand_value == 21:
        return "blackjack"
    elif player_hand_value > dealer_hand_value or dealer_hand_value > 21:
        return "player"
    elif player_hand_value == dealer_hand_value:
        return "draw"
    else:
        return "dealer"
