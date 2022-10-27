from base_classes.item import Item

class Battery(Item):
    def __init__(self, coordinates = []) -> None:
        self.name = "Battery"
        self.coordinates = coordinates