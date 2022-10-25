from base_classes.object_types import ObjectTypes

class Door:
    def __init__(self, coordinates, linked_room) -> None:
        self.graphic_char = ObjectTypes.DOOR
        self.coordinates = coordinates
        self.linked_room = linked_room
        self.linked_door = None
        
    def enter_door(self):
        return self.linked_door

    def link_door(self, door):
        self.linked_door = door