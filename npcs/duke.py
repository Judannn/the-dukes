from base_classes.npc import NPC
from base_classes.npc_reply import NPCReply
from base_classes.menu_option import MenuOption
from base_classes.item import Item
from base_classes.player import Player
from items.water import Water
from items.battery import Battery
from items.berries import Berries
from items.dog_hair import DukeHair
from items.potion import Potion

class Duke(NPC):
    '''
    A class which represents a Duke

    ...

    Methods
    -------
    talk(response, player)
        Allows a player to speak to Duke
    has_all_quest_items(player_items)
        Checks if the Player has all items to complete the quest
    '''
    def __init__(self, name, coordinates) -> None:
        '''
        Constructs all the necessary attributes for the Duke object

        Parameters
        ----------
        name : str
            the name of Duke
        coordinates : Coordinates
            the location of Duke
        '''
        super().__init__(name, coordinates)
        self.quest_accepted = False
        self.quest_complete = False

    def talk(self, response, player: Player):
        '''
        Allows a player to speak to Duke
        
        Parameters
        ----------
        response : string
        player : Player

        Returns
        ----------
        reply_details : NPCReply
        '''
        reply_details = NPCReply()
        player_items = player.item_bag[:]
        if response == f"Talk to {self.name}":
            if self.quest_complete == False:
                if self.quest_accepted == False:
                    reply_details.reply = f"{self.name}: I'm just trying to do something one second."
                    reply_details.reply_options.append(MenuOption("What are you doing?",self))
                    reply_details.reply_options.append(MenuOption("Oh ok never mind then.",self))
                else:
                    reply_details.reply = f"{self.name}: Did you find it all?"
                    reply_details.reply_options.append(MenuOption("Yep!",self))
                    reply_details.reply_options.append(MenuOption("Nope...",self))
            else:
                reply_details.reply = f"{self.name}: How's that concoction going?"
        elif response == "Yep!":
            if self.has_all_quest_items(player_items):
                reply_details.reply = f"{self.name}: Sweet, here you go!.. Dare you to drink it..."
                reply_details.item = Potion("Soupy Concoction")
                reply_details.action = f"{self.name} gives you a weird soupy concoction."
                self.quest_complete = True
                
                for item in player_items:
                    if isinstance(item, Berries) or isinstance(item, Water) or isinstance(item, Battery) or isinstance(item, DukeHair):
                        player.item_bag.remove(item)
            else:
                reply_details.reply = f"{self.name}: You don't have all the items yet. You need a battery, some animal hair, berries and some water..."
        elif response == "What are you doing?":
            reply_details.reply = f"{self.name}: I'm making this thing, I'm missing a few things though... Can you help?"
            reply_details.reply_options.append(MenuOption("Yeah sure! What do you need?",self))
            reply_details.reply_options.append(MenuOption("Nah I'm good.",self))
        elif response == "Yeah sure! What do you need?":
            self.quest_accepted = True
            player.accepted_duke_quest = True
            reply_details.reply = f"{self.name}: Ok well I need a battery, some animal hair, berries and some water, be quick!"
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = f"{self.name}: ahhh what are you doing?"
            reply_details.reply_options.append(MenuOption("Oh nothing...",self))
        elif response == "Oh nothing...":
            reply_details.reply = f"{self.name}: Cool cool cool cool..."
        return reply_details

    def has_all_quest_items(self,player_items):
        '''
        Checks if the Player has all items to complete the quest
        
        Parameters
        ----------
        player_items : []

        Returns
        ----------
        True : if has all items to complete quest
        False : if does not have all items to complete quest
        '''
        count = 0
        for item in player_items:
            if isinstance(item,Battery):
                count += 1
            elif isinstance(item,DukeHair):
                count += 1
            elif isinstance(item,Berries):
                count += 1
            elif isinstance(item,Water):
                count += 1
        if count == 4:
            return True
        else:
            return False
