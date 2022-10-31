from base_classes.item import Item

class Potion(Item):
    def __init__(self, name=None, coordinates=...) -> None:
        super().__init__(name, coordinates)
        self.name = "Concotion"
        self.coordinates = coordinates
        self.description = "A soupy concotion."
        self.empty = False
