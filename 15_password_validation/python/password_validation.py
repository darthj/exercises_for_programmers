# TODO Uhhh, this is kind of a joke it's so naive.


def get_username():
    username = input("What's your username? ")
    return username


def get_password():
    password = input("What's your password? ")
    return password


def validator(username, password):
    if password == "123abc":
        print("Welcome! ")
    else:
        print("I don't know you, {}. ".format(username))


def main():
    username = get_username()
    password = get_password()
    validator(username, password)


main()
