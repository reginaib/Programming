# read the number of observed chirps
chips_number = int(input())

# compute temperatures
temp_fahr = 50 + (chips_number - 40) / 4
temp_cels = 10 + (chips_number - 40) / 7

# print temperatures
print('temperature (Fahrenheit):', temp_fahr)
print('temperature (Celsius):', temp_cels)