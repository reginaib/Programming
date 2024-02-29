start_capital = int(input())
bet = None

while True:
    bet = input()

    if bet == 'stop':
        break

    bet_color = input()
    ball_color = input()

    if bet == "all":
        bet_amount = start_capital
    else:
        bet_amount = int(bet)

    if bet_amount > start_capital:
        print(f'You cannot bet {bet_amount} dollar if you only have {start_capital} dollar.')
        break

    if bet_color == ball_color:
        start_capital += bet_amount
    else:
        start_capital -= bet_amount

print(f'You end up with {start_capital} dollar')
