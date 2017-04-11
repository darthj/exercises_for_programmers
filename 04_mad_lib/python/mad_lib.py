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


def main():
    mad_noun = get_noun()
    mad_verb = get_verb()
    mad_adjective = get_adjective()
    mad_adverb = get_adverb()
    print_results(mad_verb, mad_adjective, mad_noun, mad_adverb)


main()
