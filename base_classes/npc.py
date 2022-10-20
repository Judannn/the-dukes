from mimetypes import init
from msilib.schema import Class


from base_classes.coordinates import Coordinates

class NPC:
    def __init__(self, name, items, coordinates) -> None:
        self.name = name
        self.items = []
        self.coordinates = coordinates
        
        for item in items: # Add items into NPC inventory
            self.items.append(item)