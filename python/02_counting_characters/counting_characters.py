def get_input():
    input_string = None

    while not input_string:
        input_string = input('What is your input string? ')
    return input_string


def print_results(input_string):
    print(input_string, 'has', len(input_string), 'characters.')


def main():
    sample_string = get_input()
    print_results(sample_string)


main()
