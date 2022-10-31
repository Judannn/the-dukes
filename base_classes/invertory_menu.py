import os
from base_classes.menu_option import MenuOption
from items.potion import Potion


class InventoryMenu:
    def __init__(self, player) -> None:
        self.player = player
        self.items = player.item_bag
        self.options = []
        self.description = ""
        self.menu_level = 1
        self.menu_loop()
    
    def menu_loop(self):
        while self.menu_level > 0:
            if not self.options:
                self.collect_item_options()
            self.print_menu()
            self.inventory_action(input())

    def inventory_action(self, player_input):
        object = self.options[int(player_input)].object
        response = self.options[int(player_input)].text
        if response == "Drink Concotion":
            self.player.drink_concotion()
            self.menu_level = 0
            self.player.action_descriptions.append("You feel super dizzy! Maybe it wasn't a great idea to drink that...")
        else:
            if object == None:
                self.options = []
                self.menu_level -= 1
                self.description = ""
            else:
                self.menu_level += 1
                self.options = []
                if isinstance(object, Potion) and not self.player.drank_concoction:
                    self.description = object.description
                    self.options.append(MenuOption("Drink Concotion",object))
                else:
                    self.description = object.description
                self.options.append(MenuOption("Exit",None))

    def collect_item_options(self):
        self.options = []
        for item in self.items:
            self.options.append(MenuOption(item.name,item))
        self.options.append(MenuOption("Exit",None))

    def print_menu(self):
        os.system('clear')
        print(f"{' ' * 10} INVENTORY {' ' * 10}")
        if not self.description == "":
            print(self.description)
        option_id = 0
        for option in self.options:
            print(f"{option_id}. {option.text}")
            option_id += 1