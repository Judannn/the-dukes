from base_classes.item import Item

class DogHair(Item):
    def __init__(self, coordinates = []) -> None:
        self.name = "Dog Hair"
        self.coordinates = coordinates