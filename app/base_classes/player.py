from nis import match
from this import d
from base_classes.door import Door
from base_classes.help_menu import HelpMenu
from base_classes.invertory_menu import InventoryMenu
from base_classes.item import Item
from base_classes.npc import NPC
from base_classes.object_types import ObjectTypes
from base_classes.player_map import PlayerMap
from base_classes.backpack import BackPack

class Player:
    '''
    A class which represents a Player

    ...

    Attributes
    ----------
    name : string
        the Player name
    graphic_char : []
        used to define the Item with a ASCII character
    item_bag : []
        defines a player item_bag
    coordinates : Coordinates
        defines the Coordinates of the Player
    current_room : Room
        defines which room the Player is in
    is_talking : bool
        defines if a Player is talking to an NPC
    action_options : []
        a list of action options available to the Player
    action_descriptions : []
        a list of action descriptions conducted by the Player
    npc_replies : []
        a list of NPC replies available to the Player
    accepted_duke_quest : bool
        defines whether the Player has accepted Dukes quest
    drank_potion : bool
        defines whether the Player has drank the Concoction
    spoke_to_dog : bool
        defines whether the Player has spoken the Dog
    spoke_to_luke : bool
        defines whether the Player has spoken to Luke
    found_murderer : bool
        defines whether the Player has found the murder.
    inventory_menu = InventoryMenu
        the player inventory menu
    help_menu : HelpMenu
        the player help menu
    player_map : PlayerMap
        the player map menu
    is_alive : bool
        is the player alive

    Methods
    -------
    player_action(player_input)
        receives a player input and acts accordinly to the input
    move(key_input)
        distributes the key_input to the correct movement direction
    move_up()
        moves the player coordinates up if possible
    move_down()
        moves the player coordinates down if possible
    move_left()
        moves the player coordinates left if possible
    move_right()
        moves the player coordinates right if possible
    pick_up_item(Item)
        picks up an item from the ground
    talk(NPC, response=None)
        talk to an NPC and returns an NPCReply
    add_action_options(options)
        adds the action options to the action_options list
    add_action_description(action_description)
        adds action descriptions to the action_descriptions list
    enter_door(door)
        moves the player into a new room through the door
    '''
    def __init__(self, name, coordinates) -> None:
        '''
        Constructs all the necessary attributes for the Player object

        Parameters
        ----------
        name : str
            the name of the Player
        coordinates : Coordinates
            the coordinates of the Player
        '''
        self.name = name
        self.graphic_char = ObjectTypes.PLAYER
        self.backpack = BackPack()
        self.item_bag = []
        self.coordinates = coordinates
        self.current_room = None
        self.is_talking = False
        self.action_options = []
        self.action_descriptions = []
        self.npc_replies = []
        self.accepted_duke_quest = False
        self.drank_potion = False
        self.spoke_to_dog = False
        self.spoke_to_luke = False
        self.found_murderer = False
        self.inventory_menu = InventoryMenu(self)
        self.help_menu = HelpMenu()
        self.player_map = PlayerMap()
        self.is_alive = True
    
    def player_action(self, player_input):
        '''
        Receives a player input and acts accordinly to the input
        
        Parameters
        ----------
        player_input : string
        '''
        if player_input.isnumeric():
            object = self.action_options[int(player_input)].object
            if isinstance(object, Item):
                self.backpack.add(object)
                self.current_room.remove_object(object)
                self.action_descriptions.append(f"You picked up a {object.name}!")
            elif isinstance(object, NPC):
                response = self.action_options[int(player_input)].text
                npc_reply = self.talk(object, response)
                if npc_reply.reply:
                    self.npc_replies.append(npc_reply.reply)
                if npc_reply.action:
                    self.action_descriptions.append(npc_reply.action)
                if npc_reply.item != None:
                    self.backpack.add(npc_reply.item)
                if npc_reply.reply_options:
                    self.action_options = []
                    self.add_action_options(npc_reply.reply_options)
                else:
                    self.is_talking = False
            elif isinstance(object, Door):
                self.enter_door(object)
        else:
            if player_input == "i":
                # open inventory menu
                self.inventory_menu.open_menu()
            elif player_input == "h":
                self.help_menu.open_help()
            elif player_input == "m":
                self.player_map.open_map()
            else:
                self.move(player_input)
    
    def move(self, key_input):
        '''
        Distributes the key_input to the correct movement direction
        
        Parameters
        ----------
        key_input : string
        '''
        self.is_talking = False
        if key_input == "w":
            self.move_up()
        elif key_input == "s":
            self.move_down()
        elif key_input == "a":
            self.move_left()
        elif key_input == "d":
            self.move_right()

    def move_up(self):
        '''Moves the player coordinates up if possible'''
        if self.coordinates.row - 1 >= 0:
            self.coordinates.row = self.coordinates.row - 1

    def move_down(self):
        '''Moves the player coordinates down if possible'''
        if self.coordinates.row + 1 <= self.current_room.rows - 1:
            self.coordinates.row = self.coordinates.row + 1

    def move_left(self):
        '''Moves the player coordinates left if possible'''
        if self.coordinates.column - 1 >= 0:
            self.coordinates.column = self.coordinates.column - 1

    def move_right(self):
        '''Moves the player coordinates right if possible'''
        if self.coordinates.column + 1 <= self.current_room.columns - 1:
            self.coordinates.column = self.coordinates.column + 1
    
    def pick_up_item(self, Item):
        '''Picks up an item from the ground'''
        self.backpack.add(Item)
    
    def talk(self, npc, response=None):
        '''
        Talk to an NPC and returns an NPCReply

        Parameters
        ----------
        npc : NPC
        response : string

        Returns
        ----------
        NPCReply
        '''
        self.is_talking = True
        return npc.talk(response,self)
    
    def add_action_options(self, options):
        '''Adds the action options to the action_options list'''
        for option in options:
            self.action_options.append(option)
    
    def add_action_description(self, action_description):
        '''Adds action descriptions to the action_descriptions list'''
        self.action_description.append(action_description)
    
    def enter_door(self, door):
        
        if door.linked_door == None:
            self.add_action_description("This door won't open...")
        else:
            # Remove player from current room
            self.current_room.remove_object(self)
            # Move player to joining door coords
            self.coordinates.row = door.linked_door.coordinates.row
            self.coordinates.column = door.linked_door.coordinates.column
            # Add player to linked room
            door.linked_room.add_object(self)