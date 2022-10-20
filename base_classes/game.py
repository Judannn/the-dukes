from base_classes.coordinates import Coordinates
from base_classes.door import Door
from base_classes.npc import NPC
from base_classes.player import Player
from base_classes.room import Room
from base_classes.item import Item
from base_classes.object_types import ObjectTypes

class Game:
    def __init__(self) -> None:
        self.player = ""
        self.continue_game = True
        self.current_room = ""
        self.setup()
        self.run()
    
    def run(self):
        while self.continue_game:
            self.current_room.update_room()
            self.current_room.print_room()
            self.player.move(input(), self.current_room)

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