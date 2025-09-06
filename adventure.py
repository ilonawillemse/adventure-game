#  adventure.py
#
#  Computer Science 50
#  Ilona Willemse
#  30-3-2022
#
#  - The main function welcomes the user and asks the user to direct through different rooms.
#  - The main function checks for input and returns the corresponding behaviour.
#  - The adventure class loads the current room and can make the user move through the rooms.
#  - The adventure class enables the user to pick up different items and drop them when whished.
#  - The adventure class also calls the descriptions of the different rooms.

import loader


class Adventure():
    # Create rooms and items for the game that was specified at the command line
    def __init__(self, filename):
        self._current_room = loader.load_room_graph(filename)
        self.items_hand = {}

    # Pass along the description of the current room, be it short or long
    def room_description(self):
        return self._current_room.description()

    # Move to a different room by changing "current" room, if possible
    def move(self, direction):
        # check whether the input direction has a connection to another room
        if not self._current_room.has_connection(direction):
            return False

        #  when there is a connection check for conditional movement (is item needed/present)
        for connection in self._current_room.get_connection(direction):
            if connection[0] == '':
                self._current_room = connection[1]
                break

            if connection[0] in self.items_hand:
                self._current_room = connection[1]
                break

        return True

    def pickup_item(self, item_object):
        # pick the wished item from the room into users hand
        self.items_hand[item_object.name] = item_object
        self._current_room.remove_item(item_object)

    def drop_item(self, item_object):
        # drop the item from users hand into the current room
        self.items_hand.pop(item_object.name)
        self._current_room.add_item(item_object)


if __name__ == "__main__":

    from sys import argv
    # Check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python3 adventure.py [name]")
        exit(1)

    # Load the requested game or else load the Tiny game
    print("Loading...")
    if len(argv) == 2:
        game_name = argv[1]
    elif len(argv) == 1:
        game_name = "Tiny"
    filename = f"data/{game_name}Adv.dat"

    # Create the game
    adventure = Adventure(filename)

    print("Welcome to Adventure.\n")
    print(adventure.room_description())

    # Prompt the user for commands
    while True:
        command = input("> ").upper()
        command = command.split(" ")

        # set the first room as visited
        adventure._current_room.set_visited()

        # load the synonyms dictionary and check for command synonyms, returning the full word
        syn_dict = loader.get_synonym()
        if command[0] in syn_dict:
            command[0] = syn_dict[command[0]]

        if command[0] == "QUIT":
            break

        # Perform the move as indicated by the user and return the description of that room when succeeded
        if command[0] in adventure._current_room.connections:

            # if the move is not possible return "not possible"
            if not adventure.move(command[0]):
                print("not possible")
            print(adventure._current_room.description())

            # when a room is entered with a forced movement, move to the correct room and print the description of that room
            while 'FORCED' in adventure._current_room.connections.keys():
                adventure.move('FORCED')
                print(adventure._current_room.description())

            # when the room has been visisted it must remember it has been
            adventure._current_room.set_visited()

            # print the items that are inside the room
            for item in adventure._current_room.items_room:
                adventure.item_string_room = adventure._current_room.items_room[item].description()
                print(adventure.item_string_room)

        # the user is being reminded of their commands and how to use them
        elif 'HELP' in command[0]:
            print('''You can move by typing directions such as EAST/WEST/IN/OUT
QUIT quits the game.
HELP prints instructions for the game.
LOOK lists the complete description of the room and its contents.
INVENTORY lists all items in your inventory.''')

        # the long description of the current room is given
        elif 'LOOK' in command[0]:
            print(adventure._current_room.description_long)
            for item in adventure._current_room.items_room:
                adventure.item_string_room = adventure._current_room.items_room[item].description()
                print(adventure.item_string_room)

        # the items currently inside your hand are returned
        elif 'INVENTORY' in command[0]:
            if len(adventure.items_hand) > 0:
                for item in adventure.items_hand:
                    adventure.item_string_hand = adventure.items_hand[item].description()
                    print(adventure.item_string_hand)
            else:
                print("Your inventory is empty")

        #  the item is taken from the room into the hand of the user
        elif 'TAKE' in command[0]:
            if len(command) < 2:
                print("Specify an item to take.")
            elif command[1] in adventure._current_room.items_room:
                adventure.pickup_item(adventure._current_room.items_room[command[1]])
                print(f'{command[1]} taken')
            else:
                print("No such item", end='')

        #  the item is dropped from the hand and put into the current room
        elif 'DROP' in command[0]:
            if command[1] in adventure.items_hand:
                adventure.drop_item(adventure.items_hand[command[1]])
                print(f'{command[1]} dropped')
            else:
                print("No such item", end='')

        # when none of the above commands are given, the command is invalid
        else:
            print("Invalid command", end='')