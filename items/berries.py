from base_classes.item import Item

class Berries(Item):
    def __init__(self, coordinates = []) -> None:
        self.name = "Berries"
        self.coordinates = coordinates