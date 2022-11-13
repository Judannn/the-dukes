import os

class HelpMenu:
    '''
    A class which represents a HelpMenu
    
    Methods
    -------
    open_help()
        Opens the help menu
    print_menu()
        Prints the help menu to console
    '''
    def __init__(self) -> None:
        pass

    def open_help(self):
        '''Opens the help menu'''
        user_input = None
        while True:
            self.print_menu()
            print("0. Exit")
            if input() == "0":
                break

    def print_menu(self):
        '''Prints the help menu to console'''
        os.system('clear')
        print(f"{' ' * 10} SYMBOLS {' ' * 10}")
        print("Player (You) - '@'")
        print("NPC - '&'")
        print("Door - 'D'")
        print("Item - '^'")
        print(f"{' ' * 10} CONTROLS {' ' * 10}")
        print("Move Forward - 'w'")
        print("Move Backward - 's'")
        print("Move Left - 'a'")
        print("Move Right - 'd'")
        print("Open Inventory - 'i'")
        print("Open Map - 'm'")
        print("Open help - 'h'")
