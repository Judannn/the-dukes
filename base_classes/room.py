from this import d
from base_classes.item import Item

class Room:
    def __init__(self, name, rows, columns):
        self.name = name
        self.object_list = []
        self.rows = rows
        self.columns = columns
        self.room = []
        self.update_room()

    def update_room(self):
        self.room = [[" " for i in range(self.rows)] for j in range(self.columns)]
        for object in self.object_list:
            xcord = object.coordinates.xcord
            ycord = object.coordinates.ycord
            self.room[xcord][ycord] = object

    def print_room(self):
        for i in self.room:
            string = ""
            for e in i:
                if e != " ":
                    string += str(e)
                else:
                    string += e
            print(string)

    def add_object(self, object):
        xcord = object.coordinates.xcord
        ycord = object.coordinates.ycord
        self.room[xcord][ycord] = object
        self.object_list.append(object)
            