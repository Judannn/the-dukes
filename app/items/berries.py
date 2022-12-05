from app.base_classes.item import Item

class Berries(Item):
    '''
    A class which represents a Berries

    ...

    Attributes
    ----------
    name : string
        the name of the Berries
    coordinates : Coordinates
        the Coordinates of the Berries
    description : string
        the description of the Berries
    '''
    def __init__(self, name=None, coordinates=...) -> None:
        '''
        Constructs all the necessary attributes for the Berries object

        Parameters
        ----------
        name : string
            the name of the Berries
        coordinates : Coordinates
            defines the Coordinates of the Berries
        '''
        super().__init__(name, coordinates)
        self.name = "Berries"
        self.coordinates = coordinates
        self.description = "Some nice juicy berries."