# read
value = int(input())
lower_bound = int(input())
upper_bound = int(input())
quality_too_low = (input())
quality_too_high = (input())

# compare and print
if value < lower_bound:
    result = f'too {quality_too_low}'
elif value > upper_bound:
    result = f'too {quality_too_high}'
else:
    result = 'just right'

print(result)
