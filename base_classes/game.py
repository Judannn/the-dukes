from re import I
from xml.etree.ElementTree import tostring
from base_classes.coordinates import Coordinates
from base_classes.door import Door
from base_classes.npc import NPC
from base_classes.player import Player
from base_classes.room import Room
from base_classes.item import Item
from base_classes.object_types import ObjectTypes
import os

class Game:
    def __init__(self) -> None:
        self.player = ""
        self.continue_game = True
        self.current_room = ""
        self.player_options = []
        self.player_actions = []
        self.player_chat = []
        self.setup()
        self.run()
    
    def run(self):
        while self.continue_game:
            os.system('clear')
            self.update_room()
            self.print_room()
            self.print_actions()
            self.print_chat()
            self.print_options()
            #player_input = self.player.move(input(""), self.current_room)
            self.player_action(input(""))

    def player_action(self, player_input):
        if player_input.isnumeric():
            object = self.player_options[int(player_input) - 1]
            if isinstance(object, Item):
                self.player.pick_up_item(object)
                self.current_room.remove_object(object)
                self.player_actions.append(f"You picked up a {object.name}!")
            elif isinstance(object, NPC):
                self.player_chat.append(self.player.talk(object))
            elif isinstance(object, Door):
                self.enter_door(object)
        else:
            self.player.move(player_input, self.current_room)
    
    def enter_door(self, door):
        door.linked_room.add_object(self.player)
        self.current_room.remove_object(self.player)
        self.current_room = door.linked_room
    
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

        # add objects to kitchen
        testroom.add_object(Item("sword",Coordinates(2,3)))
        testroom.add_object(Item("feather",Coordinates(1,1)))
        testroom.add_object(Door(Coordinates(0,2), testroom2))
        testroom.add_object(npc1)
        testroom.add_object(player1)

        #add objects to lounge
        testroom2.add_object(Door(Coordinates(0,2),testroom))

        self.current_room = testroom

    def update_room(self):
        self.room_border()
        for object in self.current_room.object_list:
            xcord = object.coordinates.xcord + 1
            ycord = object.coordinates.ycord + 1
            self.current_room.room[xcord][ycord] = object
    
    def room_border(self):
        rows = self.current_room.rows + 2
        columns = self.current_room.columns + 2
        self.current_room.room = [[" " for i in range(columns)] for j in range(rows)]
        #Add border Rows
        for xcord in range(rows):
            #Add border Columns
            for ycord in range(columns):
                if xcord == 0 or xcord == rows - 1:
                    self.current_room.room[xcord][ycord] = "─"
                if ycord == 0 or ycord == columns - 1:
                    self.current_room.room[xcord][ycord] = "│"
        
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
    
    def print_options(self):
        self.player_options = []
        option_number = 0
        for object in self.current_room.object_list:
            if(self.is_same_coord(self.player.coordinates, object.coordinates)):
                option_number +=1
                if isinstance(object, Item):
                    print(f"{option_number}. Pick up {object.name}")
                if isinstance(object, NPC):
                    print(f"{option_number}. Talk to {object.name}")
                if isinstance(object, Door):
                    print(f"{option_number}. Enter {object.linked_room.name}")
                self.player_options.append(object)
    
    def print_actions(self):
        for action in self.player_actions:
            print(action)
        self.player_actions = []
    
    def is_same_coord(self, first_coordinate, second_coordinate):
        if first_coordinate.xcord == second_coordinate.xcord:
                if first_coordinate.ycord == second_coordinate.ycord:
                    return True
        return False
    
    def print_chat(self):
        for chat in self.player_chat:
            print(chat)
        self.player_chat = []