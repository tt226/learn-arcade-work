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
    room0 = Room("You have entered the archeology room. This room contains artifacts from the void century."
                 "\nThere's a hallway to the south and room to the west.", None, 5, 4, None)
    room_list.append(room0)

    room1 = Room("You have entered the library. This small room contains a selection of the best books in the world."
                 "\nThere is hallway and rooms to the west.", None, None, None, 5)

    room_list.append(room1)

    room2 = Room("You have entered Dr. Ceasers Lab. This lab has potions for immortality."
                 "\nThere are passages to the north and the west.", 5, None, None, 3)
    room_list.append(room2)

    room3 = Room("You have entered the dining room. Ratatouille is on the menu tonight."
                 "\nThere are passages to the north, east, and west.", 5, None, 1, 2)
    room_list.append(room3)

    room4 = Room("You have entered the storge. There are armors and weapons waiting to be used."
                 "\nThere are passages to the south, east, and west.", None, 5, 1, 0)
    room_list.append(room4)

    room5 = Room("You have entered the hallway. It's dark in here."
                 "\nThere are passages to the north, south, and east.", 0, 2, 1, None)
    room_list.append(room5)
    current_room = 0

    done = False
    while done is False:

        print(room_list[current_room].description)
        way = input("Which way would you like to go? N, S, E, W\n")
# going north
        if way == "N".lower():
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way\u274C \n")
            elif next_room == room_list[current_room].north:
                print("heading north\n")
                current_room = next_room
# going south
        elif way == "S".lower():
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way\u274C \n")
            elif next_room == room_list[current_room].south:
                print("heading south\n")
                current_room = next_room
# going east
        elif way == "E".lower():
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way\u274C \n"
                      "")
            elif next_room == room_list[current_room].east:
                print("heading east\n")
                current_room = next_room
# going west
        elif way == "W".lower():
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way\u274C \n")
            elif next_room == room_list[current_room].west:
                print("heading west\n")
                current_room = next_room
# quit game
        elif way == "Q".lower():
            print("Game quit ( ˘︹˘ )")
            exit()
        else:
            print("Path doesn't exist, try again ┐(シ)┌	\n")


main()
