import unittest
import sys
sys.path.insert(0, './app')
from base_classes.game import Game

from base_classes.coordinates import Coordinates
from base_classes.door import Door
from base_classes.npc import NPC
from base_classes.player import Player
from base_classes.backpack import BackPack
from base_classes.room import Room
from base_classes.item import Item
from base_classes.menu_option import MenuOption
from base_classes.npc_reply import NPCReply

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


class TestApp(unittest.TestCase):
    """Tests game functionality"""

    # Game Test
    def test_is_same_coord(self):
        game = Game()
        self.assertTrue(game.is_same_coord(Coordinates(1,1),Coordinates(1,1)))
        self.assertFalse(game.is_same_coord(Coordinates(1,1),Coordinates(1,2)))
        
    # Player Test
    def test_item_pickup(self):
        player = Player("test",Coordinates(1,1))
        potion = Potion()
        player.pick_up_item(potion)
        test = potion in player.backpack._backpack
        self.assertTrue(test)

    # BackPack Test
    def test_item_add_and_remove(self):
        backpack = BackPack()
        potion = Potion()
        backpack.add(potion)
        test_added = potion in backpack._backpack
        self.assertTrue(test_added)
        backpack.remove
        test_removed = potion in backpack._backpack
        self.assertTrue(test_removed)

    # NPC Test
    def test_item_add(self):
        npc = NPC("test",Coordinates(1,1))
        potion = Potion()
        npc.add_item(potion)
        test = potion in npc.item_bag
        self.assertTrue(test)

    def test_can_talk(self):
        npc = NPC("test",Coordinates(1,1))
        self.assertTrue(isinstance(npc.talk("test","test"),NPCReply))

    # Room Test
    def test_object_add(self):
        room = Room("test",2,2)
        potion = Potion("test",Coordinates(1,1))
        room.add_object(potion)
        test = potion in room.object_list
        self.assertTrue(test)

if __name__ == '__main__':
    unittest.main()