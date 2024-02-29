# read the number
original_number = number = int(input())
print(number)

while number > 10 and number != 49:
    number, mod = divmod(number, 10)
    number += mod * 5
    print(number)

# print depends on if the number is divisible by 7 ( iff 7 or 49)
print(f'{original_number} is { "" if number == 7 or number == 49 else "not"} divisible by 7')





