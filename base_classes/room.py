from this import d
from base_classes.player import Player

class Room:
    def __init__(self, name, rows, columns):
        self.name = name
        self.object_list = []
        self.rows = rows
        self.columns = columns
        self.room = [[" " for i in range(self.columns)] for j in range(self.rows)]
            
    def add_object(self, object):
        xcord = object.coordinates.xcord
        ycord = object.coordinates.ycord
        self.room[xcord][ycord] = object
        self.object_list.append(object)
        # If a player add the current room to the player
        if isinstance(object, Player):
            object.current_room = self

    def remove_object(self, object):
        self.object_list.remove(object)
    
    def update_room(self):
        self.room_border()
        for object in self.object_list:
            xcord = object.coordinates.xcord + 1
            ycord = object.coordinates.ycord + 1
            self.room[xcord][ycord] = object
    
    def room_border(self):
        rows = self.rows + 2
        columns = self.columns + 2
        self.room = [[" " for i in range(columns)] for j in range(rows)]
        #Add border Rows
        for xcord in range(rows):
            #Add border Columns
            for ycord in range(columns):
                if xcord == 0 or xcord == rows - 1:
                    self.room[xcord][ycord] = "─"
                if ycord == 0 or ycord == columns - 1:
                    self.room[xcord][ycord] = "│"
