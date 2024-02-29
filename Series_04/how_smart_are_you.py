num = input()

circles_d = {
    '0': 1,
    '4': 1,
    '6': 1,
    '8': 2,
    '9': 1
}

circles = sum(circles_d.get(digit, 0) for digit in num)

print(circles)

# circles = 0
# for digit in num:
#     circles += circles_d.get(digit, 0)
# print(circles)