def has_long_words(sentence):
    if isinstance(sentence, str):  # <1>
        sentence = sentence.split(' ')

    return any(len(word) > 10 for word in sentence)
