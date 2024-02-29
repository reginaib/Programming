count = 0
max_number = -1

while True:
    serial_number = int(input())

    if serial_number < 0:
        break

    count += 1

    if serial_number > max_number:
        max_number = serial_number

t = round((count + 1) * max_number / count -1)

print(f'The number of produced tanks is estimated to be {t}.')

