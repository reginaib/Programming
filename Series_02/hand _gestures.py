#input
gesture1 = (input())
gesture2 = (input())

#rock-paper-scissors-lizard-Spock
if gesture1 == 'scissors':
    if gesture2 == 'paper' or gesture2 == 'lizard':
        result = 'player1 wins'
    elif gesture2 == 'scissors':
        result = 'draw'
    else:
        result = 'player2 wins'

if gesture1 == 'paper':
    if gesture2 == 'rock' or gesture2 == 'Spock':
        result = 'player1 wins'
    elif gesture2 == 'paper':
        result = 'draw'
    else:
        result = 'player2 wins'

if gesture1 == 'rock':
    if gesture2 == 'scissors' or gesture2 == 'lizard':
        result = 'player1 wins'
    elif gesture2 == 'rock':
        result = 'draw'
    else:
        result = 'player2 wins'

if gesture1 == 'lizard':
    if gesture2 == 'Spock' or gesture2 == 'paper':
        result = 'player1 wins'
    elif gesture2 == 'lizard':
        result = 'draw'
    else:
        result = 'player2 wins'

if gesture1 == 'Spock':
    if gesture2 == 'scissors' or gesture2 == 'rock':
        result = 'player1 wins'
    elif gesture2 == 'Spock':
        result = 'draw'
    else:
        result = 'player2 wins'

print(result)