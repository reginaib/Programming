tables_number = int(input())
amount_worth = int(input())
tables_won_doubled = int(input())
status = input()

profit = 0
value = 0

for table in range(1, tables_number):
    value += amount_worth
    profit += value
    if not table % tables_won_doubled:
        profit *= 2
        print(f'table #{table} (x2): €{profit}')
    else:
        print(f'table #{table}: €{profit}')

if status == 'lost':
    print(f'table #{tables_number}: €{profit // 2}')
else:
    value += amount_worth
    profit += value
    if not tables_number % tables_won_doubled:
        profit *= 2
        print(f'table #{tables_number} (x2): €{profit}')
    else:
        print(f'table #{tables_number}: €{profit}')
