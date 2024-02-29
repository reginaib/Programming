def isISBN(code):
    if not isinstance(code, str):
        return False

    if len(code) != 10:
        return False

    if not code[:9].isdigit():
        return False

    check_digit = int(code[0])
    for i in range(2, 10):
        check_digit += i * int(code[i - 1])
    check_digit %= 11

    # extract check digit from ISBN-10 code
    x10 = code[-1]

    return (check_digit == 10 and x10 == 'X') or x10 == str(check_digit)
