from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.menu_option import MenuOption
from base_classes.item import Item
from items.dog_hair import DogHair

class Dog(NPC):
    def __init__(self, name, coordinates) -> None:
        super().__init__(name, coordinates)
        self.has_hair = True

    def talk(self, response, player):
        reply_details = NPCReply()
        if response == f"Talk to {self.name}":
            if player.drank_concoction:
                reply_details.reply = "What's up boss?"
                reply_details.reply_options.append(MenuOption("Any idea who killed Lulu?",self))
            else:
                reply_details.reply = "woof woof!"
        elif response == "Any idea who killed Lulu?": 
            reply_details.reply = "No idea dude, but I did see a Werewolf through the garden a few times..."
            player.spoke_to_dog = True
        elif response == "Take Dog hair":
            reply_details.reply = "WOOF WOOF WOOF WOOF"
            reply_details.action = "You pull some hair from the dog... He didn't seem to like that."
            reply_details.item = DogHair("Dog Hair")
            self.has_hair = False
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = "ahhh what are you doing?"
            reply_details.reply_options.append(MenuOption("Oh nothing...",self))
        elif response == "Oh nothing...":
            reply_details.reply = "Cool cool cool cool..."
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = "Sick chain G, might have to get one myself!"
        return reply_details