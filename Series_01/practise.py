import math

raduis_str = input("Enter the radius of your circle: ")
radius_int = int(raduis_str)

circumference = 2 * math.pi * radius_int
area = math.pi * radius_int ** 2

print('The circumference is: ', circumference,
      'and the area is:', area)

fruits = ['apple', 'banana', 'cherry', 'dragonfruit']

for index, fruit in enumerate(fruits, start=1):
      print(f'{index} {fruit}')

