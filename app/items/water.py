from base_classes.item import Item

class Water(Item):
    '''
    A class which represents a Water

    ...

    Attributes
    ----------
    name : string
        the name of the Water
    coordinates : Coordinates
        the Coordinates of the Water
    description : string
        the description of the Water
    '''
    def __init__(self, name=None, coordinates=...) -> None:
        '''
        Constructs all the necessary attributes for the Water object

        Parameters
        ----------
        name : string
            the name of the Water
        coordinates : Coordinates
            defines the Coordinates of the Water
        '''
        super().__init__(name, coordinates)
        self.name = "Water"
        self.coordinates = coordinates
        self.description = "Some old fashion water."

