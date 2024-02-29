# read first nine digits of the ISBN-10 code
x1 = input()

while x1 != 'stop':
    check_digit = int(x1)
    for i in range(2, 10):
        x = int(input())
        check_digit += i * x
    check_digit %= 11

    x10 = int(input())

    if x10 == check_digit:
        print('OK')
    else:
        print('WRONG')

    x1 = input()
