import random
ACE = 11


def get_hand(deck):
    """Deals a hand"""
    first_card, deck = get_card(deck)
    second_card, deck = get_card(deck)
    cards = [first_card, second_card]
    return cards, deck


def hit(cards, deck):
    """Adds card to a hand"""
    new_card, deck = get_card(deck)
    cards.append(new_card)
    return cards, deck


def get_card(deck):
    """Deals a card"""
    card = deck[random.randint(0, len(deck)-1)]
    deck.remove(card)
    return card, deck


def get_values(cards):
    """Gets hand values from hand: '7♥' to 7; 'A♠' to 11; etc.. """
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


def get_hand_value(cards):
    """Get hands value. If hand has ace and exceeds 21, set ace to 1"""
    values = get_values(cards)
    try:
        if ACE in values and sum(values) > 21:
            values[values.index(ACE)] = 1
    except Exception as ex:
        print(ex)
    return sum(values)


def get_hand_string(cards):
    """Formats hands string"""
    card_str = ''
    for card in cards:
        card_str += f'{card} '
    return str(card_str[:len(card_str)-1])
