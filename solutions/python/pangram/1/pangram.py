def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    sentence = sentence.lower()

    letter_count = set()

    split_sentence = sentence.split()

    for word in split_sentence:

        for letter in word:

            if letter in alphabet:

                letter_count.add(letter)

    return len(letter_count) == 26
