import datetime

now = datetime.datetime.now()

current_age = int(input('What is your current age? '))
age_to_retire = int(input('At what age would you like to retire? '))

years_to_retire = age_to_retire - current_age

print('You have {:d} years to retire'.format(years_to_retire))

current_year = now.year

print('It\'s {:d},'.format(current_year), 'so you can retire in {:d}'.format(current_year + years_to_retire))