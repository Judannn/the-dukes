from base_classes.coordinates import Coordinates
from base_classes.object_types import ObjectTypes

class NPC:
    def __init__(self, name, coordinates) -> None:
        self.name = name
        self.graphic_char = ObjectTypes.NPC
        self.item_bag = []
        self.coordinates = coordinates
        
    def add_item(self, item):
        self.item_bag.append(item)

    def talk(self, player):
        return f"Hi {player.name} i'm {self.name}"