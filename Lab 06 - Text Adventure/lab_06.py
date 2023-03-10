import arcade


class Room():
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []
    room0 = Room("You have entered the archeology room. This room contains artifacts from the void century"
                 "\nThere's a hallway to the south and room to the west", None, 1, 1, None)
    room_list.append(room0)

    room1 = Room("You have entered the library. This small room contains a selection of the best books in the world"
                 "\nThere is hallway and rooms to the west", None, None, None, 3)

    room_list.append(room1)

    room2 = Room("You have entered Dr. Ceasers Lab. There are potions brewing so be careful"
                 "\nThere are passages to the north and the west", 1, None, None, 1)
    room_list.append(room2)

    room3 = Room("You have entered the dining room. Ratatouille is on the menu tonight."
                 "\n There are passages to the north, east, and west", 2, None, 1, 1)
    room_list.append(room3)

    room4 = Room("You have entered the storge. There are armors and weapons waiting to be used"
                 "\n There are passages to the south, east, and west", None, 1, 1, 1)
    room_list.append(room4)

    room5 = Room("You have entered the hallway. It's dark in here" 
                 "\n There are passages to the north, south, and east", 2, 2, 1, None)
    room_list.append(room5)
    current_room = 0

    done = False

    while done is False:

        print(room_list[current_room].description)
        input("Which way would you like to go? "
              "N, S, E, W  \n").lower()
        return

    if input("n")



main()
