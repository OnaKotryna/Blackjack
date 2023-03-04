################################
##### Ultra mega BlackJack #####
################################
from presentation import clear_view, display_card_art, display_logo, display_goodbye
from game import play


clear_view()
display_logo()
display_card_art()

input('Press enter to start')

play()
while True:
    next_game = input("Next Game? y/n\n")
    if next_game.startswith('n'):
        break
    elif next_game.startswith('y'):
        play()

display_goodbye()
