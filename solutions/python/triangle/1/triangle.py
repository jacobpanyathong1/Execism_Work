def equilateral(sides):
    """This function takes in the sides of a triangle and returns if the triangle is an equilateral triangle.

    Args:
        sides (List): all sides of a triangle

    Returns:
        _boolean_: _true/false_
    """
    equal = sides[0] == sides[1] == sides[2]
    for i in sides:
        if i == 0:
            return False
        else:
            return equal


def isosceles(sides):
    """This function takes in the sides of a triangle and returns if the triangle is an isosceles triangle.


    Args:
        sides (List): Two sides of a triangle

    Returns:
        _boolean_: _true/false_
    """
    # Check if the input list has exactly three sides
    if len(sides) != 3:
        return False
    elif not (
        sides[0] + sides[1] > sides[2]
        and sides[0] + sides[2] > sides[1]
        and sides[1] + sides[2] > sides[0]
    ):
        return False
    # Check if at least two sides are equal
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]

    pass


def scalene(sides):
    if (
        sides[0] + sides[1] <= sides[2]
        or sides[1] + sides[2] <= sides[0]
        or sides[0] + sides[2] <= sides[1]
    ):
        return False
    elif equilateral(sides) or isosceles(sides) == True:
        return False
    return True
    pass
