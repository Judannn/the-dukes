from base_classes.object_types import ObjectTypes

class Door:
    '''
    A class which represents a Door

    ...

    Attributes
    ----------
    graphic_char : ObjectType.Door
        used to define the Door with a ASCII character
    coordinates : []
        defines the Coordinates of the Door
    linked_room : Room
        the linked Room to the Door
    linked_door: Door
        the linked Door from the linked_room

    Methods
    -------
    enter_door()
        used to enter a door into the linked_room and exit at the linked_door
    link_door()
        links a door with another door
    '''
    def __init__(self, coordinates, linked_room) -> None:
        '''
        Constructs all the necessary attributes for the Door object

        Parameters
        ----------
        coordinates : []
            defines the Coordinates of the Door
        linked_room : Room
            the linked Room to the Door
        '''
        self.graphic_char = ObjectTypes.DOOR
        self.coordinates = coordinates
        self.linked_room = linked_room
        self.linked_door = None
        
    def enter_door(self):
        '''
        used to enter a door into the linked_room and exit at the linked_door

        Returns
        ----------
        Door
        '''
        return self.linked_door

    def link_door(self, door):
        '''links a door with another door'''
        self.linked_door = door