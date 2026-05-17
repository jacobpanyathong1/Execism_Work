def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    size = len(digits)
    armstrong_sum = sum([digit**size for digit in digits])
    return armstrong_sum == number
