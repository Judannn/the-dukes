from unittest import case
from base_classes.coordinates import Coordinates
from base_classes.object_types import ObjectTypes

class Player:
    def __init__(self, name, coordinates) -> None:
        self.name = name
        self.graphic_char = ObjectTypes.PLAYER
        self.item_bag = []
        self.coordinates = coordinates
        self.current_room = ""
    
    def move(self, key_input, room):
        if key_input == "u":
            self.move_up(room)
        elif key_input == "d":
            self.move_down(room)
        elif key_input == "l":
            self.move_left(room)
        elif key_input == "r":
            self.move_right(room)

    def move_up(self, room):
        if self.coordinates.xcord - 1 >= 0:
            self.coordinates.xcord = self.coordinates.xcord - 1

    def move_down(self, room):
        if self.coordinates.xcord + 1 <= room.rows - 1:
            self.coordinates.xcord = self.coordinates.xcord + 1

    def move_left(self, room):
        if self.coordinates.ycord - 1 >= 0:
            self.coordinates.ycord = self.coordinates.ycord - 1

    def move_right(self, room):
        if self.coordinates.ycord + 1 <= room.columns - 1:
            self.coordinates.ycord = self.coordinates.ycord + 1
    
    def pick_up_item(self, Item):
        self.item_bag.append(Item)
    
    def __str__(self):
        return self.graphic_char.value