temp = float(input())
light_int = float(input())

if light_int > 10000:
    result = 'supergiants (a)'
elif light_int > 1000:
    result = 'supergiants (b)'
elif light_int > 100:
    if temp < 7500:
        result = 'bright giants'
    else:
        result = 'main sequence'
elif light_int > 10:
    if temp < 6000:
        result = 'giants'
    else:
        result = 'main sequence'
elif light_int > 0.01:
    result = 'main sequence'
elif light_int > 0.0001:
    if temp > 5000:
        result = 'white dwarfs'
    else:
        result = 'main sequence'
elif light_int > 0:
    if temp > 3000:
        result = 'white dwarfs'
    else:
        result = 'main sequence'

print(result)