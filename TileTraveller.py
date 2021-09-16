# tile grid:
# 3 6 9
# 2 5 8
# 1 4 7
########
# start tile == 1
# Victory tile == 7
##########
# Movment = NESW
possible_movements = ['N','E','S','W']
current_tile = 1

def movement(way):
    if way == "N":
        return 1
    elif way == "E":
        return 3
    elif way == "S":
        return -1
    elif way == "W":
        return -3


while True:
    if current_tile == 1 or current_tile ==4:
        print('You can travel: (N)orth.')
        direction = input('Direction: ').upper()
        if direction != possible_movements[0]:
            print('Not a valid direction!')
        else:
            current_tile += movement(direction)
    
    elif current_tile ==2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        direction = input('Direction: ').upper()
        if direction != possible_movements[0] and direction != possible_movements[1] and direction !=possible_movements[2]:
            print('Not a valid direction!')
        else:
            current_tile += movement(direction)
    
    elif current_tile == 3:
        print('You can travel: (E)ast or (S)outh.')
        direction = input('Direction: ').upper()
        if direction != possible_movements[1] and direction != possible_movements[2]:
            print('Not a valid direction!')
        else:
            current_tile += movement(direction)

    elif current_tile == 5 or current_tile == 9:
        print('You can travel: (S)outh or (W)est.')
        direction = input('Direction: ').upper()
        if direction != possible_movements[2] and direction != possible_movements[3]:
            print('Not a valid direction!')
        else: current_tile += movement(direction)
    
    elif current_tile == 6:
        print('You can travel: (E)ast or (W)est.')
        direction = input('Direction: ').upper()
        if direction != possible_movements[1] and direction != possible_movements[3]:
            print('Not a valid direction!')
        else: current_tile += movement(direction)
    
    elif current_tile == 8:
        print('You can travel: (N)orth or (S)outh.')
        direction = input('Direction: ').upper()
        if direction != possible_movements[0] and direction != possible_movements[2]:
            print('Not a valid direction!')
        else: current_tile += movement(direction)
    
    elif current_tile == 7:
        print('Victory!')
        break



























