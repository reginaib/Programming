# read the input
x = int(input())

# condition
if x % 3 == 0:
    if x % 5 == 0:
        result = 'fizz buzz'
    else:
        result = 'fizz'
elif x % 5 == 0:
    result = 'buzz'
else:
    result = x

print(result)