def value(colors):
    color_list = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    value_list = [color_list.index(color) for color in colors]
    return value_list[0] * 10 + value_list[1]
