def get_age():
    age = int(input('What is your age? '))
    return age


def compare_age(age):
    if age >= 16:
        answer = "are"
    else:
        answer = "are not"
    return answer


def print_results(answer):
    print("You {} old enough to drive.".format(answer))


def main():
    age = get_age()
    compared = compare_age(age)
    print_results(compared)


main()
