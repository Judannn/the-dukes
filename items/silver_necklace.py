from base_classes.item import Item

class SilverNecklace(Item):
    def __init__(self, name=None, coordinates=...) -> None:
        super().__init__(name, coordinates)
        self.name = "Silver Necklace"
        self.coordinates = coordinates
        self.description = "A silver necklace."