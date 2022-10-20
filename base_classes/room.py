from base_classes.item import Item

class Room:
    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns
        self.room = [[" " for i in range(rows)] for j in range(columns)]

    def add_object(self, object):
            xcord = object.coordinates.xcord
            ycord = object.coordinates.ycord
            self.room[xcord][ycord] = object
            