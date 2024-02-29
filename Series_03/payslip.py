random_num = int(input())
count = 0
total = random_num

while True:
    salary = input()

    if salary == 'stop':
        break

    salary_int = int(salary)

    count += 1
    total += salary_int
    print(f'worker #{count} whispers €{total}')

avg_salary = (total - random_num) / count

print(f'average salary: €{avg_salary:.2f}')
