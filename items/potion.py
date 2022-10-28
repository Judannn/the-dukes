from base_classes.item import Item

class Potion(Item):
    def __init__(self, name=None, coordinates=...) -> None:
        super().__init__(name, coordinates)
        self.name = "Potion"
        self.coordinates = coordinates
