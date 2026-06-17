def square(number):
    if number != abs(number):
        raise ValueError(f"square must be between 1 and 64")

    if number == 0:
        raise ValueError(f"square must be between 1 and 64")

    if number > 64:
        raise ValueError(f"square must be between 1 and 64")

    grain = 2 ** (number - 1)

    return grain


def total():
    squares = 64

    total_grains = 0

    grains_on_current_square = 1

    for _ in range(squares):
        total_grains += grains_on_current_square

        grains_on_current_square *= 2

    return total_grains
