def distance(strand_a, strand_b):
    try:
        len(strand_a) == len(strand_b)
    except:
        ValueError("Strands must be of equal length.")
