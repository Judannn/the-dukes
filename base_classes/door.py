from base_classes.coordinates import Coordinates
from base_classes.object_types import ObjectTypes

class Door:
    def __init__(self, coordinates, linked_room) -> None:
        self.graphic_char = ObjectTypes.DOOR
        self.coordinates = coordinates
        self.linked_room = linked_room
        
    def __str__(self):
        return self.graphic_char.value