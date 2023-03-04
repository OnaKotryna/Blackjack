import os
import dealer
import art


def clear_view():
    """Clear window"""
    os.system('cls')


def display_logo():
    print(art.logo)


def display_card_art():
    print(art.cards)


def display_cards(player, cards):
    plr = ''
    if player.lower() == 'player':
        plr = "Your"
    if player.lower() == 'dealer':
        plr = "Dealer's"

    print(f"{plr} cards:")
    display_output(f"---- {dealer.get_hand_string(cards)} ----")
    print(f"Total: {dealer.get_hand_value(cards)}\n")


def add_dashes(dash_needed):
    dashes = '----'
    for d in dash_needed:
        dashes += '-'
    return dashes


def display_output(string):
    print(add_dashes(string))
    print("  " + string + "  ")
    print(add_dashes(string))


def display_card(player, card):
    if player.lower() == 'player':
        display_output(f"Card: {card}")
    elif player.lower() == 'dealer':
        display_output(f"Dealer's card: {card}")


def display_goodbye():
    clear_view()
    print(art.goodbye)
