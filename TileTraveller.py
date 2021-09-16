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
<<<<<<< HEAD
=======
    if locationation == 1 or locationation == 4:
        while locationation == 1 or locationation == 4:
          print("Not a valid direction!")
            Direction = input("Direction: ").upper()
            if Direction == list_of_Directions[0]:
                locationation = directions(Direction, locationation)
                return locationation  
    elif locationation == 2:
        while locationation == 2:
            print("not a valid direction!")
            direction = input("Dirction: ").upper()
            if direction == list_of_Directions[0] or direction == list_of_Directions[1] or direction == list_of_Directions[3]:
                locationation = directions(direction, locationation)
                return locationation

>>>>>>> c8cf366d05091d0135a1f01bbf89e4e0ecccf680
