from base_classes.coordinates import Coordinates

class Door:
    def __init__(self, coordinates, linked_room) -> None:
        self.coordinates = coordinates
        self.linked_room = linked_room