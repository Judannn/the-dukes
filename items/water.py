from base_classes.item import Item

class Water(Item):

    def __init__(self, name=None, coordinates=...) -> None:
        super().__init__(name, coordinates)
        self.name = "Water"
        self.coordinates = coordinates

