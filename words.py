def print_upper_words(words):
    """ This function will print out all words from the list, each on a separate line, in uppercase."""

    for word in words:
        print (word.upper())

def print_upper_words_with_e(words):
    """ This function will print out all words from the list that begin with the letter e"""

    for word in words:
        if word.lower().startswith('e'):
            print (word.upper())

def print_upper_words_with_new_letters(words, letters):
    """This function will print out all of the words in a list that begin with the input letters"""

    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                break
