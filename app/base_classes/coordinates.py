class Coordinates:
    '''
    A class which represents Coordinates

    ...

    Attributes
    ----------
    row : int
        the row coordinate
    column : int
        the column coordinate
    '''
    def __init__(self, row, column) -> None:
        '''
        Constructs all the necessary attributes for the Coordinates object

        Parameters
        ----------
        row : int
            the row coordinate
        column : int
            the column coordinate
        '''
        self.row = row
        self.column = column