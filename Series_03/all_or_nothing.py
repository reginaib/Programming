start_capital = int(input())

while True:
    bet_amount = input()

    if bet_amount == 'stop' or start_capital == 0 :
        print(f'You end up with {start_capital} dollar.')
        break

    color_bet = input()
    color_ball = input()

    if bet_amount == "all":
        bet_amount = start_capital
    else:
        bet_amount = int(bet_amount)

        if bet_amount > start_capital:
            print(f'You cannot bet {bet_amount} dollar if you only have {start_capital} dollar.')
            break

    if color_bet == color_ball:
        start_capital += bet_amount
    else:
        start_capital -= bet_amount


