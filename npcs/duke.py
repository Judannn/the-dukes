from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.menu_option import MenuOption
from base_classes.item import Item
from items.water import Water
from items.battery import Battery
from items.berries import Berries
from items.dog_hair import DogHair
from items.potion import Potion

class Duke(NPC):
    def __init__(self, name, coordinates) -> None:
        super().__init__(name, coordinates)
        self.quest_accepted = False
        self.quest_complete = False

    def talk(self, response, player):
        reply_details = NPCReply()
        if response == f"Talk to {self.name}":
            if self.quest_complete == False:
                if self.quest_accepted == False:
                    reply_details.reply = "I'm just trying to do something one second."
                    reply_details.reply_options.append(MenuOption("What are you doing?",self))
                    reply_details.reply_options.append(MenuOption("Oh ok never mind then.",self))
                else:
                    reply_details.reply = "Did you find it all?"
                    reply_details.reply_options.append(MenuOption("Yep!",self))
                    reply_details.reply_options.append(MenuOption("Nope...",self))
            else:
                reply_details.reply = "How's that concoction going?"
        elif response == "Yep!":
            if self.has_all_quest_items(player.item_bag):
                reply_details.reply = "Sweet, here you go!.. Dare you to drink it..."
                reply_details.item = Potion("Soupy Concoction")
                reply_details.action = f"{self.name} gives you a weird soupy concoction."
                self.quest_complete = True
            else:
                reply_details.reply = "You don't have all the items yet. You need a battery, some animal hair, berries and some water..."
        elif response == "What are you doing?":
            reply_details.reply = "I'm making this thing, I'm missing a few things though... Can you help?"
            reply_details.reply_options.append(MenuOption("Yeah sure! What do you need?",self))
            reply_details.reply_options.append(MenuOption("Nah I'm good.",self))
        elif response == "Yeah sure! What do you need?":
            self.quest_accepted = True
            player.accepted_duke_quest = True
            reply_details.reply = "Ok well I need a battery, some animal hair, berries and some water, be quick!"
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = "ahhh what are you doing?"
            reply_details.reply_options.append(MenuOption("Oh nothing...",self))
        elif response == "Oh nothing...":
            reply_details.reply = "Cool cool cool cool..."
        return reply_details

    def has_all_quest_items(self,player_items):
        count = 0
        for item in player_items:
            if isinstance(item,Battery):
                count += 1
            elif isinstance(item,DogHair):
                count += 1
            elif isinstance(item,Berries):
                count += 1
            elif isinstance(item,Water):
                count += 1
        if count == 4:
            return True
        else:
            return False
