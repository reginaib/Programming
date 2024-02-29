# choose random number between 1 and 10 (limits included)

import random
number = random.randint(1, 10)

# give player three turns to guess the number
guessed = False
for attempts in range(3, 0, -1):

    # ask player to make a guess
    guess = int(input(f'Make a guess ({attempts} attempts left): '))

    # test if player has guessed the correct number
    if guess == number:
            print(f'Number guessed in {3 - attempts + 1} attempts!')
            guessed = True
            break
    else:
        print('Incorrect!')

# print correct number if not guessed by player
if not guessed:
    print(f'The number was {number}.')