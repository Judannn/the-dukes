from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.menu_option import MenuOption
from base_classes.item import Item

class Daisy(NPC):
    def __init__(self, name, coordinates) -> None:
        super().__init__(name, coordinates)
    
    def talk(self, response, player):
        reply_details = NPCReply()
        if response == f"Talk to {self.name}":
            reply_details.reply = "Ahhhh get out my room!"
            reply_details.reply_options.append(MenuOption("Oh sorry!",self))
            reply_details.reply_options.append(MenuOption("Do you know anything about Lulu?",self))
        elif response == "Oh sorry!":
            reply_details.reply = "Should be! Now get out!"
        elif response == "Do you know anything about Lulu?":
            reply_details.reply = "Now is not the right time to be talking about this... Now get out!"
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = "ahhh what are you doing?"
            reply_details.reply_options.append(MenuOption("Oh nothing...",self))
        elif response == "Oh nothing...":
            reply_details.reply = "Cool cool cool cool..."
        return reply_details