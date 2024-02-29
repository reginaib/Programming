hot_days = 0
tropical_days = 0

while True:
    t = input()
    if t == 'stop':
        print('no heat wave')
        break
    t = float(t)
    if t >= 25:
        hot_days += 1
        if t > 30:
            tropical_days += 1
        if hot_days >= 5 and tropical_days >= 3:
            print('heat wave')
        break
    else:
        hot_days = 0
        tropical_days = 0
