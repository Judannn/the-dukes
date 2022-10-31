from base_classes.item import Item

class Battery(Item):
    def __init__(self, name=None, coordinates=...) -> None:
        super().__init__(name, coordinates)
        self.name = "Battery"
        self.coordinates = coordinates
        self.description = "It's a battery."
