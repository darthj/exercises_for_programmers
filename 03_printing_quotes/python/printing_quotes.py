def get_quote():
    quote = input('What is your quote? ')
    return quote


def get_person():
    person = input('Who said it? ')
    return person


def print_results(quote, person):
    print('{} says, "{}"'.format(person, quote))


if __name__ == "__main__":
    print_results(get_quote(), get_person())
