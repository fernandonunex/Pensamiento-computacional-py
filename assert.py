#assert <expression booleana>, <mensaje de error>

def first_word(letters_array):
    first_words = []

    for word in letters_array:
        assert type(word) == str, f'{word} is not a word'
        assert len(word) > 0, 'Dont´allowed empty strings'

        first_words.append(word[0])

    return first_words

letters_array = ['I','Love','You','So','Much']



print(first_word(letters_array))