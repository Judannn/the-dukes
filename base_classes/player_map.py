import os
from base_classes.menu_option import MenuOption
from items.potion import Potion

class PlayerMap:
    def __init__(self) -> None:
        self.visited_locations = []

    def open_map(self):
        while True:
            self.print_menu()
            print("0. Exit")
            if input() == "0":
                break

    def print_menu(self):
        os.system('clear')
        print(f"{' ' * 10} VISITED LOCATIONS {' ' * 10}")
        for room in self.visited_locations:
            print(room)