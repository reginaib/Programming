from datetime import date

name = input()
year_of_birth = int(input())

age = 0

while True:
    age += 1

    if age ** 2 == year_of_birth + age:
        if age ** 2 < date.today().year:
            print(f'{name} was {age} in {age ** 2}.')
        else:
            print(f'{name} turns {age} in {age ** 2}.')
        break

    elif age ** 2 > year_of_birth + age:
        print(f'{name} is not a member of the Confederacy of Squares.')
        break
