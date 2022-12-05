from app.base_classes.item import Item

class Concoction(Item):
    '''
    A class which represents a Potion

    ...

    Attributes
    ----------
    name : string
        the name of the Potion
    coordinates : Coordinates
        the Coordinates of the Potion
    description : string
        the description of the Potion
    '''
    def __init__(self, name=None, coordinates=...) -> None:
        '''
        Constructs all the necessary attributes for the Potion object

        Parameters
        ----------
        name : string
            the name of the Potion
        coordinates : Coordinates
            defines the Coordinates of the Potion

        Methods
        -------
        drink()
            drinks the concocation
        '''
        super().__init__(name, coordinates)
        self.name = "Concotion"
        self.coordinates = coordinates
        self.description = "A soupy concotion."
        self.empty = False
        
    def drink(self, player):
        player.is_alive = False
