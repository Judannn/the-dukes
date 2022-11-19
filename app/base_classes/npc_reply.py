class NPCReply:
    '''
    A class which represents a NPCReply

    ...

    Attributes
    ----------
    reply_options : []
        reply options from the NPC
    reply : string
        the reply from the NPC
    action : []
        reply actions from the NPC
    item : Item
        return of an item from the NPC
    npc : NPC
        the NPC who is replying
    '''
    def __init__(self) -> None:
        '''
        Constructs all the necessary attributes for the NPCReply object
        '''
        self.reply_options = []
        self.reply = ""
        self.action = []
        self.item = None
        self.npc = None