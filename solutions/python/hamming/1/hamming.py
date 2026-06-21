def distance(strand_a, strand_b): 
    """Find the Hamming distance between two DNA strands and returns the number of differences between them.

    Args:
        strand_a (_type_): _string_: The first DNA strand.
        strand_b (_type_): _string_: The second DNA strand.

    Raises:
        ValueError: If the two strands are not of equal length.

    Returns:
        int: The Hamming distance between the two strands.
    """
    if len(strand_a) != len(strand_b): # Check if the two strands are of equal length, if not raise a ValueError.
        
        raise ValueError("Strands must be of equal length.") # Raise a ValueError with the message "Strands must be of equal length." if the two strands are not of equal length.
    
    return sum(a != b for a, b in zip(strand_a, strand_b)) # return the Hamming distance between the two strands by summing the number of positions where the two strands differ. The zip function is used to pair up the characters from the two strands, and the sum function counts the number of pairs that are different.