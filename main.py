################################
##### Ultra mega BlackJack #####
################################
# ? Card Deck
# ? Get cards from the deck (remove taken card)
# ? Display cards
# ? Add one more card
# ? Count card values
# ? Check ACE value
# ? Get winner (pl > 21: bust; =: draw; dl < 17: +card
# ? New match
# ? Display winner
# ? Display dealer's cards

from presentation import clear_view, display_card_art, display_logo, display_goodbye
from business import play


clear_view()
display_logo()
display_card_art()

input('Press enter to start')

play()
while True:
    next_game = input("Next Game? y/n\n")
    if next_game.startswith('n'):
        break
    play()

display_goodbye()
