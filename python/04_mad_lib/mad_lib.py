def get_noun():
    noun = input('Enter a noun: ')
    return noun


def get_verb():
    verb = input('Enter a verb: ')
    return verb


def get_adjective():
    adjective = input('Enter an adjective: ')
    return adjective


def get_adverb():
    adverb = input('Enter an adverb: ')
    return adverb


def print_results(noun, verb, adjective, adverb):
    print('Do you {} your {} {} {}?\nThat\'s hilarious!'.format(verb, adjective, noun, adverb))


if __name__ == "__main__":
    print_results(get_verb(), get_adjective(), get_noun(), get_adverb())
