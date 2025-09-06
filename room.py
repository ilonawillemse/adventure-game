#  room.py
#
#  Computer Science 50
#  Ilona Willemse
#
#  - Class creates a room with a number, short description and long description.
#  - It can check whether the room has a connection with another room or item.
#  - It can check whether the room has been visited before.
#  - It can print the description with the length depending on whether the room has been visited before.

from item import Item


class Room():
    def __init__(self, number, short_description, long_description):
        self.number = number
        self._short_description = short_description
        self.description_long = long_description
        self.connections = {}
        self.items_room = {}
        self.flag = 0

    def set_visited(self):
        # mark the room as visited when it is visited
        self.flag = 1

    def description(self):
        # returns short/long description depending on whether the room has been visited before
        if self.flag == 0:
            return self.description_long
        if self.flag == 1:
            return self._short_description

    def add_connection(self, direction, item, destination_room):
        # adds a connection between the direction and item/ destination room when there is a connection
        if not self.has_connection(direction):
            self.connections[direction] = []
        self.connections[direction].append([item, destination_room])

    def has_connection(self, direction):
        # determines if there is a connection available from the room to another room, given the direction
        if direction in self.connections:
            return True
        else:
            return False

    def get_connection(self, direction):
        # retrieves the actual Room object that is found given a specific direction
        return self.connections[direction]

    def add_item(self, item_object):
        # adds an item to the room when item is supposed to be there or when user puts it there
        self.items_room[item_object.name] = item_object

    def remove_item(self, item_object):
        # removes the item from the room when it is taken by the user
        self.items_room.pop(item_object.name)