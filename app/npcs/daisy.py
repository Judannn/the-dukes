from app.base_classes.npc import NPC
from app.base_classes.npc_reply import NPCReply
from app.base_classes.menu_option import MenuOption
from app.base_classes.item import Item

class Daisy(NPC):
    '''
    A class which represents a Daisy

    ...

    Methods
    -------
    talk(response, player)
        Allows a player to speak to Daisy
    '''
    def __init__(self, name, coordinates) -> None:
        '''
        Constructs all the necessary attributes for the Daisy object

        Parameters
        ----------
        name : str
            the name of Daisy
        coordinates : Coordinates
            the location of Daisy
        '''
        super().__init__(name, coordinates)
    
    def talk(self, response, player):
        '''
        Allows a player to speak to Daisy
        
        Parameters
        ----------
        response : string
        player : Player

        Returns
        ----------
        reply_details : NPCReply
        '''
        reply_details = NPCReply()
        if response == f"Talk to {self.name}":
            reply_details.reply = f"{self.name}: Ahhhh get out my room!"
            reply_details.reply_options.append(MenuOption("Oh sorry!",self))
            reply_details.reply_options.append(MenuOption("Do you know anything about Lulu?",self))
        elif response == "Oh sorry!":
            reply_details.reply = f"{self.name}: Should be! Now get out!"
        elif response == "Do you know anything about Lulu?":
            reply_details.reply = f"{self.name}: Now is not the right time to be talking about this... Now get out!"
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = f"{self.name}: ahhh what are you doing?"
            reply_details.reply_options.append(MenuOption("Oh nothing...",self))
        elif response == "Oh nothing...":
            reply_details.reply = f"{self.name}: Cool cool cool cool..."
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = f"{self.name}: Errrr why are you pressing my necklace against me... weirdo..."
        return reply_details