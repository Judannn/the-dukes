from app.base_classes.item import Item

class Battery(Item):
    '''
    A class which represents a Battery

    ...

    Attributes
    ----------
    name : string
        the name of the Battery
    coordinates : Coordinates
        the Coordinates of the Battery
    description : string
        the description of the Battery
    '''
    def __init__(self, name=None, coordinates=...) -> None:
        '''
        Constructs all the necessary attributes for the Battery object

        Parameters
        ----------
        name : string
            the name of the Battery
        coordinates : Coordinates
            defines the Coordinates of the Battery
        '''
        super().__init__(name, coordinates)
        self.name = "Battery"
        self.coordinates = coordinates
        self.description = "It's a battery."
