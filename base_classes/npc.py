from base_classes.item import Item
from base_classes.npc_reply import NPCReply
from base_classes.object_types import ObjectTypes
from base_classes.menu_option import MenuOption

class NPC:
    '''
    A class which represents a NPC

    ...

    Attributes
    ----------
    name : string
        the name of the NPC
    graphic_char : ObjectType.NPC
        used to define the Item with a ASCII character
    item_bag : []
        a list of items the NPC carries
    coordinates : Coordinates
        the location of the NPC

    Methods
    -------
    add_item(item)
        Adds an item to the NPC item_bag
    talk(response, player)
        Allows a player to speak to the NPC
    '''
    def __init__(self, name, coordinates) -> None:
        '''
        Constructs all the necessary attributes for the NPC object

        Parameters
        ----------
        name : str
            the name of the NPC
        coordinates : Coordinates
            the location of the NPC
        '''
        self.name = name
        self.graphic_char = ObjectTypes.NPC
        self.item_bag = []
        self.coordinates = coordinates
        
    def add_item(self, item):
        '''
        Adds an item to the NPC item_bag
        
        Parameters
        ----------
        item : Item
        '''
        self.item_bag.append(item)

    def talk(self, response, player):
        '''
        Allows a player to speak to the NPC
        
        Parameters
        ----------
        response : string
        player : Player
        
        Returns
        ----------
        NPCReply
        '''
        return NPCReply()