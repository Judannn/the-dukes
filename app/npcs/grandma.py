from app.base_classes.npc import NPC
from app.base_classes.npc_reply import NPCReply
from app.base_classes.menu_option import MenuOption
from app.base_classes.item import Item

class Grandma(NPC):
    '''
    A class which represents a Grandma

    ...

    Methods
    -------
    talk(response, player)
        Allows a player to speak to Grandma
    '''
    def __init__(self, name, coordinates) -> None:
        '''
        Constructs all the necessary attributes for the Grandma object

        Parameters
        ----------
        name : str
            the name of Grandma
        coordinates : Coordinates
            the location of Grandma
        '''
        super().__init__(name, coordinates)

    def talk(self, response, player):
        '''
        Allows a player to speak to Grandma
        
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
            reply_details.reply = f"{self.name}: Oh hello deary, I'm making a coffee for the Sherrif."
        elif response == f"Press silver necklace against {self.name}":
            reply_details.action = f"You press the silver necklace against {self.name}"
            reply_details.reply = f"{self.name}: OW WHAT ARE YOU DOING!?"
            reply_details.reply_options.append(MenuOption("Why, did that hurt?",self))
        elif response == "Why, did that hurt?":
            reply_details.reply = f"{self.name}: Yes! Don't do it again."
            reply_details.reply_options.append(MenuOption("Can I ask you somthing?",self))
        elif response == "Can I ask you somthing?":
            reply_details.reply = f"{self.name}: Yes, just don't do that again."
            reply_details.reply_options.append(MenuOption("Are you a Werewolf?",self))
        elif response == "Are you a Werewolf?":
            reply_details.reply = f"{self.name}: No. Why would you think that?"
            reply_details.reply_options.append(MenuOption("*Press the necklace against her again*",self))
        elif response == "*Press the necklace against her again*":
            reply_details.reply = f"{self.name}: I TOLD YOU NOT TO DO THAT!!"
            reply_details.action = f"You press the silver necklace against {self.name} \nShe runs through the wall and of into the distance... You realise she was the murderer all along..."
            player.found_murderer = True
        return reply_details