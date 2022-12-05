from app.base_classes.item import Item

class SilverNecklace(Item):
    '''
    A class which represents a SilverNecklace

    ...

    Attributes
    ----------
    name : string
        the name of the SilverNecklace
    coordinates : Coordinates
        the Coordinates of the SilverNecklace
    description : string
        the description of the SilverNecklace
    '''
    def __init__(self, name=None, coordinates=...) -> None:
        '''
        Constructs all the necessary attributes for the SilverNecklace object

        Parameters
        ----------
        name : string
            the name of the SilverNecklace
        coordinates : Coordinates
            defines the Coordinates of the SilverNecklace
        '''
        super().__init__(name, coordinates)
        self.name = "Silver Necklace"
        self.coordinates = coordinates
        self.description = "A silver necklace."