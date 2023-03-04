from presentation import display_cards, display_output, display_card, display_card_art, clear_view
import utils


def play():
    """Game flow"""
    # start game
    player_cards, dealer_cards, deck = start()
    display_cards('player', player_cards)
    display_card("dealer", dealer_cards[0])
    # check if player wants to take card
    take_card(player_cards, dealer_cards, deck)
    # end game
    end(player_cards, dealer_cards, deck)


def start():
    """Initiates game: cleans view and returns dealt cards"""
    clear_view()
    display_card_art()
    deck = utils.deck
    return get_game_cards(deck)


def get_game_cards(deck):
    """Deals Cards"""
    player_cards, deck = utils.get_cards(deck)
    dealer_cards, deck = utils.get_cards(deck)
    return player_cards, dealer_cards, deck


def take_card(player_cards, dealer_cards, deck):
    """Checks if player wants to take one more card
        If so, deals the card"""
    while True:
        next_card = input("Take one more card? y/n\n").lower()
        # clear view
        clear_view()
        display_card_art()

        if next_card.startswith('n'):
            break
        elif next_card.startswith('y'):
            #  deals card for players
            get_card(player_cards, deck)
            # displays a dealers first card
            display_card("dealer", dealer_cards[0])


def get_card(player_cards, deck):
    """Deal's one more card and displays it"""
    player_cards, deck = utils.add_card(player_cards, deck)
    display_card("player", player_cards[-1])
    display_cards('player', player_cards)
    return player_cards, deck


def end(player_cards, dealer_cards, deck):
    """Displays game outcome"""
    winner = utils.get_winner(player_cards, dealer_cards, deck)
    display_cards('player', player_cards)
    display_cards('dealer', dealer_cards)
    if winner == 'player':
        display_output("You Won. Congrats")
    elif winner == "dealer":
        display_output("You Lost. lol")
    elif winner == 'draw':
        display_output("Pretty dissapointing, it's a draw..")
    elif winner == 'bust':
        display_output("It's a bust")
