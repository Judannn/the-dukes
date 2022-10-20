from base_classes.coordinates import Coordinates

class Player:
    def __init__(self, name, coordinates) -> None:
        self.name = name
        self.item_bag = []
        self.coordinates = coordinates
        self.current_room = ""
    
    def movement(self):
        pass
    
    def pick_up_item(self, Item):
        self.item_bag.append(Item)