from this import d
from base_classes.item import Item

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

    def remove_object(self, object):
        self.object_list.remove(object)