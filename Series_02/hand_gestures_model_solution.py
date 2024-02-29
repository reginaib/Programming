# read gestures of both players
gesture1 = input()
gesture2 = input()

# determine outcome of game
if gesture1 == gesture2:
    # draw in case both players show same gesture
    outcome = 'draw'
else:
    # determine position of gestures in list of gestures
    gestures = ['scissors', 'paper', 'rock', 'lizard', 'Spock']
    gesture1 = gestures.index(gesture1)
    gesture2 = gestures.index(gesture2)

    outcome = 'player1 wins' if gesture2 in [(gesture1 + 1) % 5, (gesture1 + 3) % 5] else 'player2 wins'
# output outcome of game
print(outcome)
