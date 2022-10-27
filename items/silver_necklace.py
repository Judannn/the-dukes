from base_classes.item import Item

class SilverNecklace(Item):
    def __init__(self, coordinates = []) -> None:
        self.name = "Silver Necklace"
        self.coordinates = coordinates