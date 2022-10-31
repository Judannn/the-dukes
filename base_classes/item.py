from base_classes.object_types import ObjectTypes

class Item:
    def __init__(self, name = None, coordinates = []) -> None:
        self.name = name
        self.graphic_char = ObjectTypes.ITEM
        self.coordinates = coordinates
        self.description = ""