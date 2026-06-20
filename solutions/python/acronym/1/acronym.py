def abbreviate(words):
    """ 
    This function takes a string of words and returns the acronym formed by the first letter of each word in uppercase.
    
    input: words (str): A string of words from which to form an acronym.
    
    output: str: The acronym formed by the first letter of each word in uppercase.
    
    """
    replaced_words = words.replace("-", " ").replace("_", " ") # treat "-" and "_" as separators
    
    split_words = replaced_words.split() # split the words on whitespace
    
    char_list = [] # create an empty list to hold the first letters of each word
    
    letter_len = len(split_words) # get the length of the split words list

    for c in range(letter_len): # loop through the split words

        if split_words[c][0].isalpha(): # check if the first character of the word is an alphabet letter

            char_list.append(split_words[c][0]) # append the first character of the word to the char_list
            
    return "".join(char_list).upper() # join the characters in char_list into a string and convert it to uppercase before returning it
