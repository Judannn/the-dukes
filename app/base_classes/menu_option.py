class MenuOption:
    '''
    A class which represents a MenuOption

    ...

    Attributes
    ----------
    text : string
        the menu option description
    object : object
        the menu options linked object
    '''
    def __init__(self, text, object) -> None:
        '''
        Constructs all the necessary attributes for the MenuOption object

        Parameters
        ----------
        text : str
            the menu option description
        object : object
            the menu options linked object
        '''
        self.text = text
        self.object = object