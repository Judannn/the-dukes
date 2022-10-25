from base_classes.coordinates import Coordinates
from base_classes.npc_reply import NPCReply
from base_classes.object_types import ObjectTypes

class NPC:
    def __init__(self, name, coordinates) -> None:
        self.name = name
        self.graphic_char = ObjectTypes.NPC
        self.item_bag = []
        self.coordinates = coordinates
        
    def add_item(self, item):
        self.item_bag.append(item)

    def talk(self, player=None, response=None):
        reply_details = NPCReply()
        if response == None:
            reply_details.reply = "What do you want!?"
            reply_details.reply_options.append("What happened here?")
            #reply_details.reply_options.append("Who did it?")
        elif response == "What happened here?":
            reply_details.reply = "Someone killed her!"
            reply_details.reply_options.append("Killed who?")
        elif response == "Who did it?":
            reply_details.reply = "Someone killed her!"
            reply_details.reply_options.append("Killed who?")
        elif response == "Killed who?":
            reply_details.reply = "Samantha!"
        return reply_details