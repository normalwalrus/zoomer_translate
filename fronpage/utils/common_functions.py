def split_words(sentence):
    split_words = sentence.split('|')
    zoomer_word = split_words[0]
    choice = split_words[1][0]
    return zoomer_word, choice
