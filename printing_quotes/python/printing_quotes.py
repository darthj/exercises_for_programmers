def get_quote():
    quote = input('What is your quote? ')
    return quote


def get_person():
    person = input('Who said it? ')
    return person


def print_results(quote, person):
    print('{} says, "{}"'.format(person, quote))


def main():
    sample = get_quote()
    icon = get_person()
    print_results(sample, icon)


main()
