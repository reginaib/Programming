num_stamps = 0
num_holes = 0
hole_cities = ''

city = input()

while city != 'finish':

    num_stamps += 1

    num_holes_in_city = city.count('🔘')

    if num_holes_in_city > 0:
        num_holes += num_holes_in_city
        hole_cities += city.replace('🔘', '') + ', '

    city = input()

if num_holes > 0:
    hole_cities = hole_cities[:-2]

# Generate the report
print(f'# stamps: {num_stamps}')
if num_holes > 0:
    print(f'# holes: {num_holes} ({hole_cities})')
else:
    print('# holes: 0')

# Determine if a cross is earned
if num_stamps == 11 and num_holes == 3:
    print('cross earned: yes')
else:
    print('cross earned: no')
