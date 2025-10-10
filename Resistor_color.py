def get_color_value_dict(color):
    colors_dict = {
  "black": 0,
  "brow"
  "n": 1,
  "red": 2,
  "orange": 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet" : 7,
    "grey" : 8,
    "white" : 9
    }

    return colors_dict.get(color, -1)

def get_color_value(color):
    if color == "black":
        return 0
    if color == "brown":
        return 1
    if color == "red":
        return 2
    if color == "orange":
        return 3
    if color == "yellow":
        return 4
    if color == "green":
        return 5
    if color == "blue":
        return 6
    if color == "violet":
        return 7
    if color == "grey":
        return 8
    if color == "white":
        return 9

color_value = get_color_value("grey")
print (color_value)

color_value = get_color_value_dict("grey")
print (color_value)