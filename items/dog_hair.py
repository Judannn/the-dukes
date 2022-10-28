from base_classes.item import Item

class DogHair(Item):
    def __init__(self, name=None, coordinates=...) -> None:
        super().__init__(name, coordinates)
        self.name = "Dog Hair"
        self.coordinates = coordinates
