import pgn
import re

game = open('sample_game.pgn').read()
preprocessed_game = pgn._pre_process_text(game)
array = []

for i in preprocessed_game:
    if i[:1] is not "[":
        current_elt = re.split(r'^([0-9]\.)', i)
        print(current_elt)
