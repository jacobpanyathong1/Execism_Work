def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if len(text) == 1:  # Handle the case where the input is a single character
        indexed_letter = alphabet.index(text)
        total_moves = (indexed_letter + key) % 26
        return alphabet[total_moves]

    elif len(text) > 1:  # Handle the case where the input has more than one character
        rotated_text = []
        for char in text:
            if (
                char.isalpha() and char.isupper()
            ):  # Process only lowercase alphabetic characters
                indexed_letter = alphabet.index(char.lower())
                total_moves = (indexed_letter + key) % 26
                rotated_text.append(alphabet[total_moves].upper())

            elif (
                char.isalpha() and char.lower()
            ):  # Process upper case alphabetic characters only.
                indexed_letter = alphabet.index(char.lower())
                total_moves = (indexed_letter + key) % 26
                rotated_text.append(alphabet[total_moves].lower())
            else:
                # Keep non-alphabet characters unchanged
                rotated_text.append(char)
        return "".join(rotated_text)

    else:
        return ""  # Handle edge case for empty strings
