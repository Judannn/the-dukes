from base_classes.item import Item

class Berries(Item):
    def __init__(self, name=None, coordinates=...) -> None:
        super().__init__(name, coordinates)
        self.name = "Berries"
        self.coordinates = coordinates
        self.description = "Some nice juicy berries."