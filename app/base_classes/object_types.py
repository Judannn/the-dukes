from enum import Enum
from colorama import Fore

class ObjectTypes(Enum):
    """
    Object type ENUMS defines object with character.
    """
    DOOR = Fore.LIGHTYELLOW_EX + "D" 
    ITEM = Fore.CYAN + "^"
    NPC = Fore.GREEN + "&" 
    PLAYER = Fore.MAGENTA + "@"