def translate(text):
    vowels = ["a", "e", "i", "o", "u"]
    sometimes_vowel = ["y"]
    split_text = text.split()

    translated_words = []

    for word in split_text:
        if word[0] in vowels or word[:2] in ["xr", "yt"]:
            translated_words.append(word + "ay")
        else:
            consonant_cluster = ""
            i = 0
            while i < len(word) and (
                word[i] not in vowels and (word[i] != "y" or i == 0)
            ):
                if word[i : i + 2] == "qu":
                    consonant_cluster += "qu"
                    i += 2
                else:
                    consonant_cluster += word[i]
                    i += 1

            translated_word = word[i:] + consonant_cluster + "ay"
            translated_words.append(translated_word)

    return " ".join(translated_words)
