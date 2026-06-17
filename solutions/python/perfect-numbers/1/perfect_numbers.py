def classify(number):
    """A perfect number equals the sum of its positive divisors (excluding itself).

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # Calculate sum of factors (excluding the number itself)
    factor_list = [i for i in range(1, number) if number % i == 0]
    factor_sum = sum(factor_list)

    # Classify the number based on the sum of its factors
    if factor_sum == number:
        return "perfect"
    elif factor_sum > number:
        return "abundant"
    else:
        return "deficient"
