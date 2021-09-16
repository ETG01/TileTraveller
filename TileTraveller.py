list_of_Directions = "NSWE"
position = 1
victory = False

def directions(way, locationation):
    if way == "N":
        locationation = locationation + 1
    elif way == "S":
        locationation = locationation - 1
    elif way == "W":
        locationation = locationation - 3
    elif way == "E":
        locationation = locationation + 3
    return locationation


def error(locationation):
