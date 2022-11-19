from base_classes.object_types import ObjectTypes

class Item:
    '''
    A class which represents a Item

    ...

    Attributes
    ----------
    name : string
        the Item name
    graphic_char : ObjectType.Item
        used to define the Item with a ASCII character
    coordinates : Coordinates
        the location of the NPC
    description : string
        a description of the Item
    '''
    def __init__(self, name = None, coordinates = []) -> None:
        '''
        Constructs all the necessary attributes for the Player object

        Parameters
        ----------
        name : string
            the Item name
        coordinates : Coordinates
            the location of the NPC
        '''
        self.name = name
        self.graphic_char = ObjectTypes.ITEM
        self.coordinates = coordinates
        self.description = ""