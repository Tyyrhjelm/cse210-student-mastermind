import random

class Board:
    """The responsability of Board is to keep track of the pieces in play.
    
    Stereotype:
        Information Holder
    
    
    """
    
    def __init__(self):
        """The class constructor."""
        pass


    def prepare(self, player):
        
        """Sets up the board with an entry for each of tne players.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    
