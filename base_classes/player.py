from nis import match
from base_classes.door import Door
from base_classes.item import Item
from base_classes.npc import NPC
from base_classes.object_types import ObjectTypes

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
    
    def player_action(self, player_input):
        if player_input.isnumeric():
            object = self.action_options[int(player_input) - 1].object
            if isinstance(object, Item):
                self.pick_up_item(object)
                self.current_room.remove_object(object)
                self.action_descriptions.append(f"You picked up a {object.name}!")
            elif isinstance(object, NPC):
                response = self.action_options[int(player_input)].text
                npc_reply = self.talk(object, response)
                self.npc_replies.append(npc_reply.reply)
                if npc_reply.item != None:
                    self.action_descriptions.append(npc_reply.action)
                    self.pick_up_item(npc_reply.item)
                if npc_reply.reply_options:
                    self.action_options = []
                    self.add_action_options(npc_reply.reply_options)
                else:
                    self.is_talking = False
            elif isinstance(object, Door):
                self.enter_door(object)
        else:
            self.move(player_input, self.current_room)
    
    def move(self, key_input, room):
        self.is_talking = False
        if key_input == "u":
            self.move_up(room)
        elif key_input == "d":
            self.move_down(room)
        elif key_input == "l":
            self.move_left(room)
        elif key_input == "r":
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
        return npc.talk(response)
    
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
            # Move player to joining door coords
            self.coordinates.row = door.linked_door.coordinates.row
            self.coordinates.column = door.linked_door.coordinates.column
            # Add player to linked room
            door.linked_room.add_object(self)
            # Remove player from current room
            self.current_room.remove_object(self)
            # Update linked room to current room
            self.current_room = door.linked_room