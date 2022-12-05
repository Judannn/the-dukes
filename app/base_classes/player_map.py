import os
from app.base_classes.menu_option import MenuOption
from app.items.potion import Potion

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
    add_visited_locations()
        Updates which room the player has been in
    write_visited_locations()
        Writes which rooms the player has been in to a text file
    '''
    def __init__(self) -> None:
        self.empty_box = u'\u2610'
        self.cross_box = u'\u2612'
        self.visited_locations = []
        self.visited_locations.append(f"{self.empty_box} : Kitchen")
        self.visited_locations.append(f"{self.empty_box} : Study")
        self.visited_locations.append(f"{self.empty_box} : Bedroom")
        self.visited_locations.append(f"{self.empty_box} : Bathroom")
        self.visited_locations.append(f"{self.empty_box} : Dining Room")
        self.visited_locations.append(f"{self.empty_box} : Hallway")
        self.visited_locations.append(f"{self.empty_box} : Bedroom 2")
        self.visited_locations.append(f"{self.empty_box} : Bedroom 3")
        self.visited_locations.append(f"{self.empty_box} : Garden")
        self.visited_locations.append(f"{self.empty_box} : Shed")
        self.write_visited_locations()

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
    
    def add_visited_location(self, room):
        '''Updates which room the player has been in'''
        for location in self.visited_locations:
            if location == f"{self.empty_box} : {room.name}":
                index = self.visited_locations.index(f"{self.empty_box} : {room.name}")
                self.visited_locations[index] = f"{self.cross_box} : {room.name}"
                self.write_visited_locations()

    def write_visited_locations(self):
        '''Writes which rooms the player has been in to a text file'''
        with open('./visited_locations.txt', 'w') as text_file:
            text_file.write("Visited Locations;\n")
            for location in self.visited_locations:
                text_file.write(f"{location}\n")
