import os
from xml.etree.ElementTree import tostring
from base_classes.coordinates import Coordinates
from base_classes.door import Door
from base_classes.npc import NPC
from base_classes.player import Player
from base_classes.room import Room
from base_classes.item import Item
from base_classes.object_types import ObjectTypes
from base_classes.player_option import PlayerOption
from items.berries import Berries
from items.water import Water
from items.battery import Battery
from items.dog_hair import DogHair
from items.potion import Potion
from items.silver_necklace import SilverNecklace

from npcs.daisy import Daisy
from npcs.duke import Duke
from npcs.grandma import Grandma
from npcs.dog import Dog
from npcs.luke import Luke
from npcs.sherrif_rosco import SherrifRoscoe

class Game:
    def __init__(self) -> None:
        self.player = None
        self.continue_game = True
        self.setup()
        self.run()
    
    def run(self):
        while self.continue_game:
            os.system('clear')
            self.current_room.update_room()
            self.print_room()
            if self.player.is_talking != True:
                self.player.action_options = self.collect_action_options()
            self.print_npc_replies()
            self.print_action_descriptions()
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

        # create npc's
        daisy = Daisy("Daisy",Coordinates(3,2))
        duke = Duke("Duke",Coordinates(3,2))
        grandma = Grandma("Grandma",Coordinates(3,2))
        dog = Dog("Dog",Coordinates(3,2))
        luke = Luke("Luke",Coordinates(3,2))
        sherrif_roscoe = SherrifRoscoe("Sherrif Roscoe",Coordinates(3,2))

        # add items to player
        duke.add_item(Potion)
        dog.add_item(DogHair)

        # create rooms
        kitchen = Room("Kitchen",4,4)
        study = Room("Study",6,4)
        bedroom1 = Room("Bedroom",4,5)
        bathroom = Room("Bathroom",4,3)
        dining_room = Room("Dining Room",4,6)
        hallway = Room("Hallway",3,10)
        bedroom2 = Room("Bedroom 2",4,5)
        bedroom3 = Room("Bedroom 3",4,5)
        garden = Room("Garden",4,7)
        shed = Room("Shed",4,4)

        # create doors
        kitchen_door = Door(Coordinates(3,2), dining_room)
        dining_room_door1 = Door(Coordinates(0,2), kitchen)
        dining_room_door2 = Door(Coordinates(1,5), hallway)
        hallway_door1 = Door(Coordinates(0,1), dining_room)
        hallway_door2 = Door(Coordinates(0,0), study)
        study_door = Door(Coordinates(2,3), hallway)
        hallway_door3 = Door(Coordinates(0,4), bedroom1)
        bedroom1_door = Door(Coordinates(3,2), hallway)
        hallway_door4 = Door(Coordinates(0,8), bathroom)
        bathroom_door = Door(Coordinates(3,1), hallway)
        hallway_door5 = Door(Coordinates(2,2), bedroom2)
        bedroom2_door = Door(Coordinates(0,2), hallway)
        hallway_door6 = Door(Coordinates(2,7), bedroom3)
        bedroom3_door = Door(Coordinates(0,2), hallway)
        hallway_door7 = Door(Coordinates(1,9), garden)
        garden_door1 = Door(Coordinates(1,0), hallway)
        garden_door2 = Door(Coordinates(1,6), shed)
        shed_door = Door(Coordinates(1,0), garden)


        # link doors
        kitchen_door.link_door(dining_room_door1)
        dining_room_door1.link_door(kitchen_door)
        dining_room_door2.link_door(hallway_door1)
        hallway_door1.link_door(dining_room_door2)
        hallway_door2.link_door(study_door)
        study_door.link_door(hallway_door2)
        hallway_door3.link_door(bedroom1_door)
        bedroom1_door.link_door(hallway_door3)
        hallway_door4.link_door(bathroom_door)
        bathroom_door.link_door(hallway_door4)
        hallway_door5.link_door(bedroom2_door)
        bedroom2_door.link_door(hallway_door5)
        hallway_door6.link_door(bedroom3_door)
        bedroom3_door.link_door(hallway_door6)
        hallway_door7.link_door(garden_door1)
        garden_door1.link_door(hallway_door7)
        garden_door2.link_door(shed_door)
        shed_door.link_door(garden_door2)

        # kitchen add objects
        kitchen.add_object(Water(Coordinates(0,0)))
        kitchen.add_object(kitchen_door)
        kitchen.add_object(grandma)

        # dining room add objects
        dining_room.add_object(sherrif_roscoe)
        dining_room.add_object(dining_room_door1)
        dining_room.add_object(dining_room_door2)
        dining_room.add_object(player1)

        # hallway add objects
        hallway.add_object(hallway_door1)
        hallway.add_object(hallway_door2)
        hallway.add_object(hallway_door3)
        hallway.add_object(hallway_door4)
        hallway.add_object(hallway_door5)
        hallway.add_object(hallway_door6)
        hallway.add_object(hallway_door7)

        # bedroom1 add objects
        bedroom1.add_object(bedroom1_door)
        bedroom1.add_object(daisy)
        bedroom1.add_object(SilverNecklace(Coordinates(0,0)))

        # bathroom add objects
        bathroom.add_object(bathroom_door)
        bathroom.add_object(luke)

        # bedroom2 add objects
        bedroom2.add_object(bedroom2_door)
        bedroom2.add_object(Battery(Coordinates(0,3)))

        # bedroom3 add objects
        bedroom3.add_object(bedroom3_door)

        # garden add objects
        garden.add_object(garden_door1)
        garden.add_object(garden_door2)
        garden.add_object(dog)
        garden.add_object(Berries(Coordinates(0,3)))

        # shed add objects
        garden.add_object(shed_door)
        garden.add_object(duke)

        self.current_room = dining_room

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
        if first_coordinate.row == second_coordinate.row:
                if first_coordinate.column == second_coordinate.column:
                    return True
        return False

    def print_room(self):
        print(f"Current Room: {self.current_room.name}")
        for i in self.player.current_room.room:
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