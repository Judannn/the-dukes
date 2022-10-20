from base_classes.player import Player
from base_classes.coordinates import Coordinates

class Item:
    def __init__(self, name, graphic_char, coordinates) -> None:
        self.name = name
        self.graphic_char = graphic_char
        self.coordinates = coordinates