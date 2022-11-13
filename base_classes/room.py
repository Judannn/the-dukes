from this import d
from base_classes.player import Player
from colorama import Fore
from graphics import graphics

class Room:
    '''
    A class which represents a Room

    ...

    Attributes
    ----------
    name : string
        the room name
    object_list : []
        a list of objects that are in the room
    rows : int
        defines the height of the room
    columns : int
        defines the width of the room
    room : []
        an array which defines the height and width of the room

    Methods
    -------
    add_object(object)
        Adds an object to the list of objects in this Room
    remove_object(object)
        Removes an object from the list of objects in this Room
    update_room()
        Updates the object locations in the Room
    room_border()
        Used to add a graphical border around the Room
    '''
    def __init__(self, name, rows, columns):
        '''
        Constructs all the necessary attributes for the Room object

        Parameters
        ----------
        name : str
            the name of the Room
        rows : int
            the height of the Room
        columns : int
            the width of the Room
        '''
        self.name = name
        self.object_list = []
        self.rows = rows
        self.columns = columns
        self.room = [[" " for i in range(self.columns)] for j in range(self.rows)]
            
    def add_object(self, object):
        '''
        Adds an object to the list of objects in this Room
        
        Parameters
        ----------
        object : object
        '''
        row = object.coordinates.row
        column = object.coordinates.column
        self.room[row][column] = object
        self.object_list.append(object)
        # If a player add the current room to the player
        if isinstance(object, Player):
            object.current_room = self

    def remove_object(self, object):
        '''
        Removes an object from the list of objects in this Room
        
        Parameters
        ----------
        object : object
        '''
        self.object_list.remove(object)
    
    def update_room(self):
        '''Updates the object locations in the Room'''
        self.room_border()
        for object in self.object_list:
            row = object.coordinates.row + 1
            column = object.coordinates.column + 1
            self.room[row][column] = object
    
    def room_border(self):
        '''Used to add a graphical border around the Room'''
        rows = self.rows + 2
        columns = self.columns + 2
        self.room = [[" " for i in range(columns)] for j in range(rows)]
        #Add border Rows
        for row in range(rows):
            #Add border Columns
            for column in range(columns):
                if column == 0: # Left
                    self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.left_border
                if column == columns -1: # Right
                    self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.right_border
                if row == 0 or row == rows - 1:
                    if row == 0 and column == 0: # Top left corner
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.top_left_border
                    elif row == rows -1 and column == 0: # Bottom left corner
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.bottom_left_border
                    elif row == 0 and column == columns - 1: # Top right corner
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.top_right_border
                    elif row == rows -1 and column == columns -1: # Bottom right corner
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.bottom_right_border
                    elif row == 0: # Top
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.top_border
                    elif row == rows - 1: # Bottom
                        self.room[row][column] = Fore.LIGHTWHITE_EX +  graphics.bottom_border
