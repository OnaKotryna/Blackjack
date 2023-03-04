import random

deck = [
    '1♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    '1♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '1♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    '1♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
]

ACE = 11


def get_cards(deck):
    first_card, deck = get_card(deck)
    second_card, deck = get_card(deck)
    player_cards = [first_card, second_card]
    return player_cards, deck


def get_card(deck):
    card = deck[random.randint(0, len(deck)-1)]
    deck.remove(card)
    return card, deck


def add_card(cards, deck):
    new_card, deck = get_card(deck)
    cards.append(new_card)
    return cards, deck


def get_values(cards):
    values = []
    for card in cards:
        try:
            card_val = str(card[:len(card)-1])
            if card_val.isnumeric():
                values.append(int(card_val))
            elif card_val == 'A':
                values.append(11)
            else:
                values.append(10)
        except Exception as ex:
            print(ex)
    return values


def get_card_sum(cards):
    values = get_values(cards)
    try:
        if ACE in values and sum(values) > 21:
            values[values.index(ACE)] = 1
    except Exception as ex:
        print(ex)
    return sum(values)


def get_winner(player_cards, dealer_cards, deck):
    player = get_card_sum(player_cards)
    if player > 21:
        return "bust"

    dealer = get_card_sum(dealer_cards)
    if dealer < 17:
        card, deck = get_card(deck)
        dealer_cards.append(card)
        dealer = get_card_sum(dealer_cards)

    if player > dealer or dealer > 21:
        return "player"
    elif player == dealer:
        return "draw"
    else:
        return "dealer"


def get_card_string(cards):
    card_str = ''
    for card in cards:
        card_str += f'{card} '
    return str(card_str[:len(card_str)-1])
