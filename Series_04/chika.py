# read the number
number = input()
print(number)
result = ''
# save the value of the first number to print it in the end
number_print = number


# loop to make provided operations
for digit in number:
    while int(number) != 49 and int(number) > 10:
        result = str(int(number[:-1]) + int(number[-1]) * 5)
        print(result)
        # reassign the number
        number = result

# print depends on if the number is divisible by 7 ( iff 7 or 49)
if int(number_print) % 7:
    print(f'{number_print} is not divisible by 7')
else:
    print(f'{number_print} is divisible by 7')





