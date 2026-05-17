"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word

    pass


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    vocab_prefix = vocab_words[0]

    new_list = []

    for word in vocab_words:

        new_list.append(vocab_prefix + word)

    new_list[0] = vocab_prefix

    split_list = [part for element in new_list for part in element.split(" ")]

    result_string = " :: ".join(split_list)

    return result_string
    pass


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word.endswith("ness"):

        removed_suffix = word[:-4]  # Remove the last 4 characters

    else:

        removed_suffix = word

    # Replace "i" with "y" in the modified word
    if removed_suffix.endswith("i"):

        new_word = removed_suffix[:-1] + "y"
    else:
        return removed_suffix

    return new_word
    pass


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    clean_sentence = sentence.replace(".", "")

    split_sentence = clean_sentence.split()

    replacement_word = split_sentence[index]

    replaced_word = replacement_word.replace(replacement_word, replacement_word + "en")

    return replaced_word
    pass
