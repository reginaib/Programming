# read the digits
age_dif = int(input())
years_from_now = int(input())
times_older = int(input())

# calculate son's and mother's age in months
age_son_months = (age_dif + years_from_now - years_from_now*times_older) * 12 // (times_older - 1)
age_mom_months = age_son_months + (age_dif * 12)

# print the results
print('The mother is', age_mom_months, 'months old and her son', age_son_months, 'months.')