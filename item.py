# item.py
#
#  Computer Science 50
#  Ilona Willemse
#
#  - Class creates an item with name and description.

class Item():

    def __init__(self, name, item_description):
        self.name = name
        self.item_description = item_description

    def description(self):
        return(f"{self.name}, {self.item_description}")