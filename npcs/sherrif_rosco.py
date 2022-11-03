from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.menu_option import MenuOption
from base_classes.item import Item

class SherrifRoscoe(NPC):
    def __init__(self, name, coordinates) -> None:
        super().__init__(name, coordinates)

    def talk(self, response, player):
        reply_details = NPCReply()
        if response == f"Talk to {self.name}":
            reply_details.reply = "What do you want!?"
            reply_details.reply_options.append(MenuOption("What happened here?",self))
            reply_details.reply_options.append(MenuOption("Who did it?",self))
        elif response == "What happened here?":
            reply_details.reply = "Someone killed her!"
            reply_details.reply_options.append(MenuOption("Killed who?",self))
        elif response == "Killed who?":
            reply_details.reply = "Samantha!"
        elif response == "Who did it?":
            reply_details.reply = "I don't bloody know, I'm trying to figure it out..."
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = "Buddy, Pal, you're a bit weird arn't you. Stop bothering me now alright..."
        return reply_details