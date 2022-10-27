from xml.etree.ElementTree import tostring
from base_classes.coordinates import Coordinates
from base_classes.door import Door
from base_classes.npc import NPC
from base_classes.player import Player
from base_classes.room import Room
from base_classes.item import Item
from base_classes.object_types import ObjectTypes
from base_classes.player_option import PlayerOption
import os

class Game:
    def __init__(self) -> None:
        self.player = None
        self.continue_game = True
        self.current_room = None
        self.setup()
        self.run()
    
    def run(self):
        while self.continue_game:
            os.system('clear')
            self.current_room.update_room()
            self.print_room()
            if self.player.is_talking != True:
                self.player.action_options = self.collect_action_options()
            self.print_action_descriptions()
            self.print_npc_replies()
            self.print_action_options()
            #player_input = self.player.move(input(""), self.current_room)
            while True:
                player_input = input()
                if player_input == "u" or player_input == "d" or player_input == "l" or player_input == "r" or self.player.action_options and int(player_input) <= len(self.player.action_options)-1:
                    break
                else:
                    self.print_console()
            self.player.player_action(player_input)

    def print_console(self):
        os.system('clear')
        self.print_room()
        self.print_action_descriptions()
        self.print_npc_replies()
        self.print_action_options()
    
    def setup(self):
        # create Player
        player1 = Player("Jourdan",Coordinates(3,3))
        self.player = player1

        # create npc
        npc1 = NPC("John",Coordinates(3,2))

        # add items to player
        npc1.add_item(Item("potion"))

        # create rooms
        testroom = Room("Kitchen",4,4)
        testroom2 = Room("lounge",6,4)

        # create doors
        door1 = Door(Coordinates(0,2), testroom2)
        door2 = Door(Coordinates(5,3), testroom)

        # link doors
        door1.link_door(door2)
        door2.link_door(door1)

        # add objects to kitchen
        testroom.add_object(Item("sword",Coordinates(2,3)))
        testroom.add_object(Item("feather",Coordinates(1,1)))
        
        door1.link_door(door2)
        testroom.add_object(door1)
        
        testroom.add_object(npc1)
        testroom.add_object(player1)

        #add objects to lounge
        testroom2.add_object(door2)

        self.current_room = testroom

    def collect_action_options(self):
        options = []
        for object in self.current_room.object_list:
            if(self.is_same_coord(self.player.coordinates, object.coordinates)):
                if isinstance(object, Item):
                    options.append(PlayerOption(f"Pick up {object.name}", object))
                if isinstance(object, NPC):
                    options.append(PlayerOption(f"Talk to {object.name}", object))
                if isinstance(object, Door):
                    options.append(PlayerOption(f"Enter {object.linked_room.name}", object))
        return options

    def is_same_coord(self, first_coordinate, second_coordinate):
        if first_coordinate.xcord == second_coordinate.xcord:
                if first_coordinate.ycord == second_coordinate.ycord:
                    return True
        return False

    def print_room(self):
        print(f"Current Room: {self.current_room.name}")
        for i in self.current_room.room:
            string = ""
            for e in i:
                if(isinstance(e, str)):
                    string += e
                else:
                    string += e.graphic_char.value
            print(string)
    
    def print_action_options(self):
        option_id = 0
        for option in self.player.action_options:
            print(f"{option_id}. {option.text}")
            option_id += 1
    
    def print_action_descriptions(self):
        for action in self.player.action_descriptions:
            print(action)
        self.player.action_descriptions = []
    
    def print_npc_replies(self):
        for chat in self.player.npc_replies:
            print(chat)
        self.player.npc_replies = []

    # def collect_action_options(self):
    #     self.player_options = []
    #     for object in self.current_room.object_list:
    #         if(self.is_same_coord(self.player.coordinates, object.coordinates)):
    #             if isinstance(object, Item):
    #                 self.add_player_option(f"Pick up {object.name}", object)
    #             if isinstance(object, NPC):
    #                 self.add_player_option(f"Talk to {object.name}", object)
    #             if isinstance(object, Door):
    #                 self.add_player_option(f"Enter {object.linked_room.name}", object)

    # def player_action(self, player_input):
    #     if player_input.isnumeric():
    #         object = self.player_options[int(player_input) - 1].object
    #         if isinstance(object, Item):
    #             self.player.pick_up_item(object)
    #             self.current_room.remove_object(object)
    #             self.player_actions.append(f"You picked up a {object.name}!")
    #         elif isinstance(object, NPC):
    #             response = self.player_options[int(player_input)].text
    #             npc_reply = self.player.talk(object, response)
    #             self.player_chat.append(npc_reply.reply)
    #             if npc_reply.item != None:
    #                 self.player_actions.append(npc_reply.action)
    #                 self.player.pick_up_item(npc_reply.item)
    #             if npc_reply.reply_options:
    #                 self.player_options = []
    #                 self.add_player_options(npc_reply.reply_options)
    #             else:
    #                 self.player.talking = False
    #         elif isinstance(object, Door):
    #             self.enter_door(object)
    #     else:
    #         self.player.move(player_input, self.current_room)
    
    # def enter_door(self, door):
    #     if door.linked_door == None:
    #         self.player_actions.append("This door won't open...")
    #     else:
    #         # Move player to joining door coords
    #         self.player.coordinates.xcord = door.linked_door.coordinates.xcord
    #         self.player.coordinates.ycord = door.linked_door.coordinates.ycord
    #         # Add player to linked room
    #         door.linked_room.add_object(self.player)
    #         # Remove player from current room
    #         self.current_room.remove_object(self.player)
    #         # Update linked room to current room
    #         self.current_room = door.linked_room

    # def update_room(self):
    #     self.room_border()
    #     for object in self.current_room.object_list:
    #         xcord = object.coordinates.xcord + 1
    #         ycord = object.coordinates.ycord + 1
    #         self.current_room.room[xcord][ycord] = object
    
    # def room_border(self):
    #     rows = self.current_room.rows + 2
    #     columns = self.current_room.columns + 2
    #     self.current_room.room = [[" " for i in range(columns)] for j in range(rows)]
    #     #Add border Rows
    #     for xcord in range(rows):
    #         #Add border Columns
    #         for ycord in range(columns):
    #             if xcord == 0 or xcord == rows - 1:
    #                 self.current_room.room[xcord][ycord] = "─"
    #             if ycord == 0 or ycord == columns - 1:
    #                 self.current_room.room[xcord][ycord] = "│"
        
    # def print_room(self):
    #     print(f"Current Room: {self.current_room.name}")
    #     for i in self.current_room.room:
    #         string = ""
    #         for e in i:
    #             if(isinstance(e, str)):
    #                 string += e
    #             else:
    #                 string += e.graphic_char.value
    #         print(string)