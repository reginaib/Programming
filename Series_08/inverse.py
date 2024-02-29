# birds that need to be counted
birds = [' tern', ' goose', ' goose', ' hawk',
         'tern', 'tern', ' goose']
# build a dictionary of frequencies
observations = {}
for bird in birds:
    # dict.get : fetch bird observations
    # with default value 0
    observations[bird] = observations.get(bird, 0) + 1

# invert dictionary
inverse = {}
for key , value in observations.items():
    birds = inverse.get(value, [])
    birds.append(key)
    inverse[value] = birds

# display dictionary in sorted order
for count in sorted(inverse):
    print(count, inverse[count])