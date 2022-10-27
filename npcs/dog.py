from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.player_option import PlayerOption
from base_classes.item import Item

class Dog(NPC):
    def __init__(self, name, coordinates) -> None:
        super().__init__(name, coordinates)