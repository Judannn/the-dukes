from base_classes.item import Item

class Potion(Item):
    def __init__(self, coordinates = []) -> None:
        self.name = "Potion"
        self.coordinates = coordinates