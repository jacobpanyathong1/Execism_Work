def is_paired(input_string):
    """This function inputs a string and finds the opening and closing matching bracket
    and returns True or False output.

    Args:
        input_string (_type_): str

    Returns:
        True or False
    """

    # empty stack to keep track of opening brackets
    stack = []

    # mapping of closing brackets to their corresponding opening brackets
    pairs = {")": "(", "]": "[", "}": "{"}

    # iterate through each character in the input string
    for c in input_string:

        # if the character is an opening bracket, push it onto the stack
        if c in "([{":

            # append the opening bracket to the stack
            stack.append(c)

        # if the character is a closing bracket, check if it matches the last opening bracket on the stack
        elif c in pairs and (not stack or stack.pop() != pairs[c]):

            return False

    return len(stack) == 0
