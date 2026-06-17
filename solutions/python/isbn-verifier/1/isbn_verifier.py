def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10 or not (
        isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == "X")
    ):
        return False
    total = 0
    for i in range(10):
        if isbn[i] == "X":
            total += 10 * (10 - i)
        else:
            total += int(isbn[i]) * (10 - i)

    return total % 11 == 0
