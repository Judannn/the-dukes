from this import d
from base_classes.player import Player
from colorama import Fore

class Room:
    def __init__(self, name, rows, columns):
        self.name = name
        self.object_list = []
        self.rows = rows
        self.columns = columns
        self.room = [[" " for i in range(self.columns)] for j in range(self.rows)]
            
    def add_object(self, object):
        row = object.coordinates.row
        column = object.coordinates.column
        self.room[row][column] = object
        self.object_list.append(object)
        # If a player add the current room to the player
        if isinstance(object, Player):
            object.current_room = self

    def remove_object(self, object):
        self.object_list.remove(object)
    
    def update_room(self):
        self.room_border()
        for object in self.object_list:
            row = object.coordinates.row + 1
            column = object.coordinates.column + 1
            self.room[row][column] = object
    
    def room_border(self):
        rows = self.rows + 2
        columns = self.columns + 2
        self.room = [[" " for i in range(columns)] for j in range(rows)]
        #Add border Rows
        for row in range(rows):
            #Add border Columns
            for column in range(columns):
                if column == 0:
                    self.room[row][column] = Fore.LIGHTWHITE_EX +  "     ░▒▓╣"
                if column == columns -1:
                    self.room[row][column] = Fore.LIGHTWHITE_EX +  "╠▓▒░"
                if row == 0 or row == rows - 1:
                    if row == 0 and column == 0:
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  "     ░▒▓╬"
                    elif row == rows -1 and column == 0:
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  "     ░▒▓╬"
                    elif row == 0 and column == columns - 1:
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  "╬▓▒░"
                    elif row == rows -1 and column == columns -1:
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  "╬▓▒░"
                    elif row == 0:
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  "╩"
                    elif row == rows - 1:
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  "╦"
