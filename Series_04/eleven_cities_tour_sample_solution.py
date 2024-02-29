# initialize reported information
stamps = 0  # number of stamps
holes = 0  # number of holes
cities = ''  # list of city names with holes

stamp = input()

while stamp != 'finish':

    # count additional stamp
    stamps += 1

    # count additional holes
    holes += stamp.count('🔘')

    # add stamp with holes to list of cities
    if ' ' in stamp:
        stamp = stamp.replace('🔘 ', '')
        cities += stamp + ', '

    # read next stamp
    stamp = input()

# format cities with holes
if cities:
    cities = f' ({cities.rstrip(", ")})'

# check if cross is earned
cross = 'yes' if stamps == 11 and holes == 3 else 'no'

# output formatted report
print(f'# stamps: {stamps}')
print(f'# holes: {holes}{cities}')
print(f'cross earned: {cross}')
