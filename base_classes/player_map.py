import os
from base_classes.menu_option import MenuOption
from items.potion import Potion

class PlayerMap:
    '''
    A class which represents a PlayerMap

    ...

    Attributes
    ----------
    visited_locations : [] 
        a list of locations the player has visited

    Methods
    -------
    open_map()
        Opens the player map menu
    print_menu()
        Prints the player map menu to console
    '''
    def __init__(self) -> None:
        self.visited_locations = []

    def open_map(self):
        '''Opens the player map menu'''
        while True:
            self.print_menu()
            print("0. Exit")
            if input() == "0":
                break

    def print_menu(self):
        '''Prints the player map menu to console'''
        os.system('clear')
        print(f"{' ' * 10} VISITED LOCATIONS {' ' * 10}")
        for room in self.visited_locations:
            print(room)