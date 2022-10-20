from base_classes.player import Player
from base_classes.object_types import ObjectTypes
from base_classes.coordinates import Coordinates

class Item:
    def __init__(self, name, coordinates = []) -> None:
        self.name = name
        self.graphic_char = ObjectTypes.ITEM
        self.coordinates = coordinates

    def __str__(self):
        return self.graphic_char.value