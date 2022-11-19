import inspect
from locale import LC_MESSAGES
import os
import time
from xml.etree.ElementTree import tostring
from colorama import Fore

from graphics import graphics

from base_classes.coordinates import Coordinates
from base_classes.door import Door
from base_classes.npc import NPC
from base_classes.player import Player
from base_classes.room import Room
from base_classes.item import Item
from base_classes.menu_option import MenuOption

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
    '''
    A class which represents a Game

    ...

    Attributes
    ----------
    player : Player
        the player reference for the game
    continue_game : bool
        used to check if game is complete or not

    Methods
    -------
    new_game()
        Prepares a new game to be played, runs through intro, setup then into gameplay
    game_intro()
        Plays the intro to the game where the username of the player is asked
    run()
        Runs all gameplay code in order to play the game
    finish_game()
        Runs the outro then stops the game once the player presses any key
    collect_action_options()
        Returns a list of player options for any object the player is standing on
    has_silver_necklace()
        Checks if the player has a silver necklace in there item_bag
    is_same_coord(first_coordinate, second_coordinate)
        Checks if two coordinates are the same
    print_console()
        Prints all game info into the console
    print_room()
        Prints the players current room to console
    print_action_options()
        Prints the players current actions options available to console
    print_action_descriptions()
        Prints the players action desciptions to console
    print_npc_replies()
        Prints npc's reply options to console
    type_write(print_string, timing)
        Prints to console but in a typewriter style by clearing the console
    setup(player_name)
        Instantiates all class objects required for the game
    '''

    def __init__(self) -> None:
        '''Constructs all the necessary attributes for the Game object'''
        self.player = None
        self.continue_game = True
    
    def new_game(self):
        '''Prepares a new game to be played, runs through the intro, setup then into gameplay'''
        self.player = None
        self.continue_game = True
        player_name = self.game_intro()
        self.setup(player_name)
        self.run()
    
    def game_intro(self):
        '''
        Plays the intro to the game and asks for a username from the player

        Returns
        ----------
        string : the players user name
        '''
        os.system('clear')
        print(graphics.heading_logo)
        print(Fore.RED + "                    A Murder Mystery Game                         ")
        print()
        player_name = input(Fore.WHITE + "Please enter your player name:\n")
        self.type_write(f"Welcome {player_name}\nThere seems to have been a murder in the Dukes house.\nSee if you can find out who it was...\nFor help with controls press 'h'\nGood Luck!...",0.05)
        time.sleep(2)

        return player_name

    def run(self):
        '''Runs all gameplay code in order to play the game'''
        while self.continue_game:
            os.system('clear')
            self.print_room()
            if self.player.is_talking != True:
                self.player.action_options = self.collect_action_options()
            self.print_npc_replies()
            self.print_action_descriptions()
            self.print_action_options()
            while True:
                player_input = input(Fore.WHITE + "Input: ").lower()
                if player_input.isnumeric():
                    if self.player.action_options and int(player_input) <= len(self.player.action_options)-1:
                        break
                elif player_input == "w" or player_input == "a" or player_input == "s" or player_input == "d" or player_input == "i" or player_input == "m" or player_input == "h":
                    break
                self.print_console()
            self.player.player_action(player_input)
            if self.player.found_murderer: # Check if player has found the murderer
                self.finish_game(True)
            if not self.player.is_alive: # Check if the player has died
                self.finish_game(False)
    
    def finish_game(self, has_found_murderer):
        '''Runs the outro then stops the game once the player presses any key'''
        os.system('clear')
        print(graphics.heading_logo)
        print(Fore.RED + "                    A Murder Mystery Game                         ")
        if has_found_murderer:
            print()
            self.type_write(f"You press the silver necklace against Grandma She runs through the wall and of into the distance...\nYou realise she was the murderer all along...\nSo {self.player.name} you figured it out... Until next time...",0.05)
            print()
        else:
            print()
            self.type_write(f"You suddenly die...\nMaybe it was something to do with that soupy concoction...\nSo {self.player.name} Until next time...",0.05)
            print()
        play_again = input("Press Y to play again or any other key to exit.\n").lower() == "y"
        if play_again:
            self.new_game()
        else:
            self.continue_game = False

    def collect_action_options(self):
        '''
        Returns a list of player options for any object the player is standing on

        Returns
        ----------
        [] : List of action options
        '''
        options = []
        for object in self.player.current_room.object_list:
            if self.is_same_coord(self.player.coordinates, object.coordinates) and not isinstance(object, Player):
                if isinstance(object, Item):
                    options.append(MenuOption(f"Pick up {object.name}", object))
                if isinstance(object, NPC):
                    options.append(MenuOption(f"Talk to {object.name}", object))
                    if isinstance(object, Dog) and object.has_hair and self.player.accepted_duke_quest:
                        options.append(MenuOption(f"Take Dog hair", object))
                    elif self.player.spoke_to_luke and self.has_silver_necklace:
                        options.append(MenuOption(f"Press silver necklace against {object.name}", object))
                if isinstance(object, Door):
                    options.append(MenuOption(f"Enter {object.linked_room.name}", object))
        return options

    def has_silver_necklace(self):
        '''
        Checks if the player has a silver necklace in their item_bag
        
        Returns
        ----------
        True : if player has a silver necklace
        False : if player doesn't have a silver necklace
        '''
        for item in self.player.item_bag:
            if isinstance(item, SilverNecklace):
                return True
        return False

    def is_same_coord(self, first_coordinate, second_coordinate):
        '''
        Checks if two coordinates are the same
        
        Parameters
        ----------
        first_coordinate : Coordinate
        second_coordinate : Coordinate

        Returns
        ----------
        True : if coordinates match
        False : if coordinates don't match
        '''
        if first_coordinate.row == second_coordinate.row:
                if first_coordinate.column == second_coordinate.column:
                    return True
        return False

    def print_console(self):
        '''Prints all game info into the console'''
        os.system('clear')
        self.print_room()
        self.print_action_descriptions()
        self.print_npc_replies()
        self.print_action_options()

    def print_room(self):
        '''Prints the players current room to console'''
        self.player.current_room.update_room()
        print(Fore.RED + f"Current Room: {self.player.current_room.name}")
        for i in self.player.current_room.room:
            string = ""
            for e in i:
                if(isinstance(e, str)):
                    string += e
                else:
                    string += e.graphic_char.value
            print(string)
    
    def print_action_options(self):
        '''Prints the players current actions options available to console'''
        if self.player.action_options:
            option_id = 0
            for option in self.player.action_options:
                print(Fore.WHITE + f"{option_id}. {option.text}")
                option_id += 1
    
    def print_action_descriptions(self):
        '''Prints the players action desciptions to console'''
        if self.player.action_descriptions:
            for action in self.player.action_descriptions:
                print(Fore.WHITE + action)
            self.player.action_descriptions = []
    
    def print_npc_replies(self):
        '''Prints npc's reply options to console'''
        if self.player.npc_replies:
            for chat in self.player.npc_replies:
                print(Fore.WHITE + chat)
            self.player.npc_replies = []

    def type_write(self, print_string, timing):
        '''
        Prints to console but in a typewriter style by clearing the console

        Parameters
        ----------
        print_string : string
        timing : float
        '''
        string = ""
        for chr in print_string:
            os.system('clear')
            print(graphics.heading_logo)
            print(Fore.RED + "                    A Murder Mystery Game                         ",)
            print(Fore.WHITE + string)
            string += chr
            time.sleep(timing)

    def setup(self, player_name):
        '''
        Instantiates all class objects required for the game

        Parameters
        ----------
        player_name : string
        '''
        # Create Player
        player1 = Player(player_name,Coordinates(3,3))
        self.player = player1

        # # comment out below when not testing
        # player1.pick_up_item(Potion("Concoction"))
        # player1.pick_up_item(SilverNecklace("Silver Necklace"))
        # player1.pick_up_item(Berries("Berries"))
        # player1.pick_up_item(Water("Water"))
        # player1.pick_up_item(Battery("Battery"))
        # player1.pick_up_item(DogHair("Dog Hair"))
        # player1.spoke_to_dog = True
        # player1.spoke_to_luke = True

        # create npc's
        daisy = Daisy("Daisy",Coordinates(1,2))
        duke = Duke("Duke",Coordinates(2,1))
        grandma = Grandma("Grandma",Coordinates(1,2))
        dog = Dog("Dog",Coordinates(2,4))
        luke = Luke("Luke",Coordinates(2,1))
        sherrif_roscoe = SherrifRoscoe("Sherrif Roscoe",Coordinates(1,2))

        # add items to player
        duke.add_item(Potion)
        dog.add_item(DogHair)

        # create rooms
        kitchen = Room("Kitchen",4,4)
        study = Room("Study",4,4)
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
        hallway_door1 = Door(Coordinates(1,0), dining_room)
        hallway_door2 = Door(Coordinates(0,0), study)
        study_door = Door(Coordinates(3,2), hallway)
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
        kitchen.add_object(Water(coordinates=Coordinates(0,0)))
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

        # study add objects
        study.add_object(study_door)

        # bedroom1 add objects
        bedroom1.add_object(bedroom1_door)
        bedroom1.add_object(daisy)
        bedroom1.add_object(SilverNecklace(coordinates=Coordinates(0,0)))

        # bathroom add objects
        bathroom.add_object(bathroom_door)
        bathroom.add_object(luke)

        # bedroom2 add objects
        bedroom2.add_object(bedroom2_door)
        bedroom2.add_object(Battery(coordinates=Coordinates(0,3)))

        # bedroom3 add objects
        bedroom3.add_object(bedroom3_door)

        # garden add objects
        garden.add_object(garden_door1)
        garden.add_object(garden_door2)
        garden.add_object(dog)
        garden.add_object(Berries(coordinates=Coordinates(0,3)))

        # shed add objects
        shed.add_object(shed_door)
        shed.add_object(duke)