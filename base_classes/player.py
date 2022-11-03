from nis import match
from this import d
from base_classes.door import Door
from base_classes.help_menu import HelpMenu
from base_classes.invertory_menu import InventoryMenu
from base_classes.item import Item
from base_classes.npc import NPC
from base_classes.object_types import ObjectTypes
from base_classes.player_map import PlayerMap
from npcs.dog import Dog

class Player:
    def __init__(self, name, coordinates) -> None:
        self.name = name
        self.graphic_char = ObjectTypes.PLAYER
        self.item_bag = []
        self.coordinates = coordinates
        self.current_room = None
        self.is_talking = False
        self.action_options = []
        self.action_descriptions = []
        self.npc_replies = []
        self.accepted_duke_quest = False
        self.drank_concoction = False
        self.spoke_to_dog = False
        self.spoke_to_luke = False
        self.found_murderer = False
        self.inventory_menu = InventoryMenu(self)
        self.help_menu = HelpMenu()
        self.player_map = PlayerMap()
    
    def player_action(self, player_input):
        if player_input.isnumeric():
            object = self.action_options[int(player_input)].object
            if isinstance(object, Item):
                self.pick_up_item(object)
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
                    self.pick_up_item(npc_reply.item)
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
                self.move(player_input, self.current_room)
    
    def move(self, key_input, room):
        self.is_talking = False
        if key_input == "w":
            self.move_up(room)
        elif key_input == "s":
            self.move_down(room)
        elif key_input == "a":
            self.move_left(room)
        elif key_input == "d":
            self.move_right(room)

    def move_up(self, room):
        if self.coordinates.row - 1 >= 0:
            self.coordinates.row = self.coordinates.row - 1

    def move_down(self, room):
        if self.coordinates.row + 1 <= room.rows - 1:
            self.coordinates.row = self.coordinates.row + 1

    def move_left(self, room):
        if self.coordinates.column - 1 >= 0:
            self.coordinates.column = self.coordinates.column - 1

    def move_right(self, room):
        if self.coordinates.column + 1 <= room.columns - 1:
            self.coordinates.column = self.coordinates.column + 1
    
    def pick_up_item(self, Item):
        self.item_bag.append(Item)
    
    def talk(self, npc, response=None):
        self.is_talking = True
        return npc.talk(response,self)
    
    def add_action_options(self, options):
        for option in options:
            self.action_options.append(option)
    
    def remove_action_options(self):
        self.action_options = []
    
    def add_action_description(self, action_description):
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
            if not door.linked_room.name in self.player_map.visited_locations:
                self.player_map.visited_locations.append(f"{door.linked_room.name}")
    
    def drink_concotion(self):
        self.drank_concoction = True