from app.base_classes.npc import NPC
from app.base_classes.npc_reply import NPCReply
from app.base_classes.menu_option import MenuOption
from app.base_classes.item import Item

class SherrifRoscoe(NPC):
    '''
    A class which represents a SherrifRoscoe

    ...

    Methods
    -------
    talk(response, player)
        Allows a player to speak to SherrifRoscoe
    '''
    def __init__(self, name, coordinates) -> None:
        '''
        Constructs all the necessary attributes for the SherrifRoscoe object

        Parameters
        ----------
        name : str
            the name of SherrifRoscoe
        coordinates : Coordinates
            the location of SherrifRoscoe
        '''
        super().__init__(name, coordinates)

    def talk(self, response, player):
        '''
        Allows a player to speak to SherrifRoscoe
        
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
            reply_details.reply = f"{self.name}: What do you want!?"
            reply_details.reply_options.append(MenuOption("What happened here?",self))
            reply_details.reply_options.append(MenuOption("Who did it?",self))
        elif response == "What happened here?":
            reply_details.reply = f"{self.name}: Someone killed her!"
            reply_details.reply_options.append(MenuOption("Killed who?",self))
        elif response == "Killed who?":
            reply_details.reply = f"{self.name}: Lulu!"
        elif response == "Who did it?":
            reply_details.reply = f"{self.name}: I don't bloody know, I'm trying to figure it out..."
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = f"{self.name}: Buddy, Pal, you're a bit weird arn't you. Stop bothering me now alright..."
        return reply_details