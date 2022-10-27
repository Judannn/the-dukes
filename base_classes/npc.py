from base_classes.item import Item
from base_classes.npc_reply import NPCReply
from base_classes.object_types import ObjectTypes
from base_classes.player_option import PlayerOption

class NPC:
    def __init__(self, name, coordinates) -> None:
        self.name = name
        self.graphic_char = ObjectTypes.NPC
        self.item_bag = []
        self.coordinates = coordinates
        
    def add_item(self, item):
        self.item_bag.append(item)

    def talk(self, response):
        pass