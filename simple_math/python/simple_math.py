first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

fmt_str = '{:d} {} {:d} = {}'

print(fmt_str.format(first_number, '+', second_number, first_number + second_number))
print(fmt_str.format(first_number, '-', second_number, first_number - second_number))
print(fmt_str.format(first_number, '*', second_number, first_number * second_number))
print(fmt_str.format(first_number, '/', second_number, first_number / second_number))
