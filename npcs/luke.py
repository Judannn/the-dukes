from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.menu_option import MenuOption
from base_classes.item import Item

class Luke(NPC):
    def __init__(self, name, coordinates) -> None:
        super().__init__(name, coordinates)

    def talk(self, response, player):
        reply_details = NPCReply()
        if response == f"Talk to {self.name}":
            reply_details.reply = f"{self.name}: Hey {player.name} what's up?"
            if player.drank_concoction:
                reply_details.reply_options.append(MenuOption("I heard there was a Werewolf sighting out in the garden?!",self))
            reply_details.reply_options.append(MenuOption("Any idea who killed Lulu?",self))
        elif response == "I heard there was a Werewolf sighting out in the garden?!":
            reply_details.reply = f"{self.name}: What a joke, next you'll be telling me we need some more silver around the house... maybe we should tell Sherrif Rosco to get some silver bullets haha!"
            player.spoke_to_luke = True
            reply_details.reply_options.append(MenuOption(f"Cheers for the sarcasm {self.name}",self))
        elif response == f"Cheers for the sarcasm {self.name}":
            reply_details.reply = f"{self.name}: Sorry dude i'm just trying to lighten the mood."
        elif response == "Any idea who killed Lulu?":
            reply_details.reply = f"{self.name}: No idea man, it's honestly a bit scary it was right outside my window and I heard nothing!"
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = f"{self.name}: Ok I wasn't being serious when I said we should get some more silver..."
        return reply_details