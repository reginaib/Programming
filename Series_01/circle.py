from math import acos, sin, cos, radians

# read the input values in degrees
x1_d = float(input())
y1_d = float(input())
x2_d = float(input())
y2_d = float(input())

r = 6371

# convert degrees to radians
x1 = radians(x1_d)
y1 = radians(y1_d)
x2 = radians(x2_d)
y2 = radians(y2_d)

# calculate the great-circle distance d
value = sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2)
# guarantee that value is in interval [-1, 1]
value = max(-1.0, min(value, 1.0))
d = (r * acos(value))
d = round(d)

# print the results
print(f'The great-circle distance is {d} km.')
