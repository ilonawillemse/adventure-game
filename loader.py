#  loader.py
#
#  Computer Science 50
#  Ilona Willemse
#
#  - The function load_room_graph loads a file and reads the rooms, connections and items available.
#  - The function load_room_graph also makes connections between the rooms and the items inside the rooms.
#  - The function get_synonym reads the data from a file and stores it into a dictionary.

from room import Room
from item import Item


def load_room_graph(filename):
    # creates a graph of all room objects pointing to each other and returns a reference to the "first" rooms
    # stores room information in a dictionary that maps a room number to a room object
    # create a new room object using the data from the list
    rooms = {}

    with open(filename) as f:
        # loop through the rooms
        while True:
            line = f.readline()
            if line == "\n":
                break
            line = line.split("\t")

            # create a new room object
            number = int(line[0])
            short_description = line[1]
            long_description = line[2]
            room_object = Room(number, short_description, long_description)

            # add the room object to a rooms dictionary
            rooms[number] = room_object

        # hard check whether program does what it should
        assert 1 in rooms
        assert rooms[1]._short_description == "Outside building"

        # loop through the directions
        while True:
            direction_line = f.readline()
            if direction_line == "\n":
                break

            direction_line = direction_line.split("\t")

            # save the current room into variable
            source_room = rooms[int(direction_line[0])]

            # add the connection combinations of rooms and items
            for i in range(1, len(direction_line), 2):
                direction = direction_line[i]
                destination = direction_line[i + 1]

                # when conditional movement item is present
                if '/' in destination:
                    destination = destination.split('/')
                    destination_room = rooms[int(destination[0])]
                    item = destination[1]

                else:
                    destination_room = rooms[int(direction_line[i + 1])]
                    item = ''

                # add the connection
                source_room.add_connection(direction, item, destination_room)

        # loop through the items
        while True:
            item_line = f.readline()
            if len(item_line) == 0:
                break

            item_line = item_line.split("\t")
            # create a new item object using the data from the list containing an item and description
            item_object = Item(item_line[0], item_line[1])
            rooms[int(item_line[2])].add_item(item_object)

        # returns the first room to start the game with
        return rooms[1]


def get_synonym():
    # function loads synonyms from a file into a dictionary and returns the dictionary
    synonyms_dict = {}

    with open('data/Synonyms.dat') as f:
        while True:
            synonym = f.readline()
            if len(synonym) == 0:
                break
            synonym = synonym.split("=")
            synonyms_dict[synonym[0]] = synonym[1].rstrip()

    return synonyms_dict