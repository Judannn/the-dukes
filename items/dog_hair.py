import sys
sys.path.insert(0,"..")
from base_classes.item import Item

class battery(Item):
    def __init__(self, xcord, ycord) -> None:
        super().__init__()
        self.name = "Battery"
        self.xcord = xcord
        self.ycord = ycord