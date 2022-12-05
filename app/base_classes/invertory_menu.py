import os
from app.base_classes.menu_option import MenuOption
from app.items.potion import Potion
from app.items.concoction import Concoction


class InventoryMenu:
    '''
    A class which represents a InventoryMenu

    ...

    Attributes
    ----------
    player : Player
        the Player linked the InventoryMenu
    options : []
        a list of inventory options
    description : string
        a item description
    menu_level : int
        defines the menu level currently accessed

    Methods
    -------
    setup()
        Prepares the inventory menu for use
    open_menu()
        Opens the inventory menu
    inventory_action(player_input)
        Receives a player input and acts accordinly to the input
    collect_item_options()
        Collects item options for the user
    print_menu()
        Prints menu to console
    '''
    def __init__(self, player) -> None:
        '''
        Constructs all the necessary attributes for the Player object

        Parameters
        ----------
        player : Player
            the Player linked the InventoryMenu
        '''
        self.player = player
        self.options = []
        self.description = ""
        self.menu_level = 1
    
    def setup(self):
        '''Prepares the inventory menu for use'''
        self.options = []
        self.description = ""
        self.menu_level = 1
    
    def open_menu(self):
        '''Opens the inventory menu'''
        self.setup()
        while self.menu_level > 0:
            if not self.options:
                self.collect_item_options()
            self.print_menu()
            self.inventory_action(input())

    def inventory_action(self, player_input):
        '''
        Receives a player input and acts accordinly to the input
        
        Parameters
        ----------
        player_input : string
        '''
        object = self.options[int(player_input)].object
        response = self.options[int(player_input)].text
        if self.menu_level == 2 and isinstance(object, Potion):
            object.drink(self.player)
            self.menu_level = 0
            self.player.action_descriptions.append("You feel super dizzy! Maybe it wasn't a great idea to drink that...")
        elif self.menu_level == 2 and isinstance(object, Concoction):
            object.drink(self.player)
            self.menu_level = 0
        else:
            if object == None:
                self.options = []
                self.menu_level -= 1
                self.description = ""
            else:
                self.menu_level += 1
                self.options = []
                if isinstance(object, Potion) and not self.player.drank_potion:
                    self.description = object.description
                    self.options.append(MenuOption(f"Drink {object.name}",object))
                elif isinstance(object, Concoction):
                    self.description = object.description
                    self.options.append(MenuOption(f"Drink {object.name}",object))
                else:
                    self.description = object.description
                self.options.append(MenuOption("Exit",None))

    def collect_item_options(self):
        '''Collects item options for the user'''
        self.options = []
        for item in self.player.backpack.list():
            self.options.append(MenuOption(item.name,item))
        self.options.append(MenuOption("Exit",None))

    def print_menu(self):
        '''Prints menu to console'''
        os.system('clear')
        print(f"{' ' * 10} INVENTORY {' ' * 10}")
        if not self.description == "":
            print(self.description)
        option_id = 0
        for option in self.options:
            print(f"{option_id}. {option.text}")
            option_id += 1