from base_classes.item import Item

class DogHair(Item):
    '''
    A class which represents a DogHair

    ...

    Attributes
    ----------
    name : string
        the name of the DogHair
    coordinates : Coordinates
        the Coordinates of the DogHair
    description : string
        the description of the DogHair
    '''
    def __init__(self, name=None, coordinates=...) -> None:
        '''
        Constructs all the necessary attributes for the DogHair object

        Parameters
        ----------
        name : string
            the name of the DogHair
        coordinates : Coordinates
            defines the Coordinates of the DogHair
        '''
        super().__init__(name, coordinates)
        self.name = "Dog Hair"
        self.coordinates = coordinates
        self.description = "A tuff of dog hair."
