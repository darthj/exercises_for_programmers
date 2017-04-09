def get_name():
    name = input('What is your name? ')
    return name


def print_name(name):
    print('Hello {}, nice to meet you!'.format(name))


def main():
    your_name = get_name()
    print_name(your_name)


main()
