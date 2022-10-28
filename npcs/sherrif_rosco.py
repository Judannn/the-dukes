from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.player_option import PlayerOption
from base_classes.item import Item

class SherrifRoscoe(NPC):
    def __init__(self, name, coordinates) -> None:
        super().__init__(name, coordinates)

    def talk(self, response):
        reply_details = NPCReply()
        if response == f"Talk to {self.name}":
            reply_details.reply = "What do you want!?"
            reply_details.reply_options.append(PlayerOption("What happened here?",self))
            reply_details.reply_options.append(PlayerOption("Who did it?",self))
            reply_details.reply_options.append(PlayerOption("Can I grab a drink?",self))
        elif response == "What happened here?":
            reply_details.reply = "Someone killed her!"
            reply_details.reply_options.append(PlayerOption("Killed who?",self))
        elif response == "Killed who?":
            reply_details.reply = "Samantha!"
        elif response == "Who did it?":
            reply_details.reply = "I don't bloody know..."
        elif response == "Can I grab a drink?":
            reply_details.reply = "Anything else champ?"
            reply_details.action = f"{self.name} gives you a bottle of water."
            reply_details.reply_options.append(PlayerOption("Nah I'm good",self))
            reply_details.item = Item("Water Bottle")
        return reply_details