class PlayerResponse:
    '''
    A class which represents a PlayerResponse

    ...

    Attributes
    ----------
    response : string
        the player response
    player_items : []
        the player response items
    '''
    def __init__(self) -> None:
        '''Constructs all the necessary attributes for the PlayerResponse object'''
        self.response = None
        self.player_items = None