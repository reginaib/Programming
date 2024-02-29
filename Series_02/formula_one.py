import math

# read the input
grand_prix = (input())
lap_distance_km = float(input())
avg_lap = float(input())

if grand_prix == 'Monaco':
    number_of_laps = 78
    total_race_dist = 260.52
else:
    number_of_laps = math.ceil(305.0 / lap_distance_km)
    total_race_dist = round(number_of_laps * lap_distance_km, 3)
    time = avg_lap * number_of_laps
    if time > 120:
        number_of_laps = math.ceil(120 / avg_lap)
        total_race_dist = number_of_laps * lap_distance_km

print(f'The Grand Prix of {grand_prix} runs over {number_of_laps} laps ({total_race_dist} km).')










