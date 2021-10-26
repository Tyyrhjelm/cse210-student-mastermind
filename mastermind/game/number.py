import random
#this should generate a secret random number between 1000 and 9999
#this is the number the players are trying to guess.  this is already done in board though.


class Code:
    """The responsibility of this class is to generate a secret random number between 1000 and 9999 """

    def code_number(self):

        self.code_number = random.randint(1000, 9999)

        return self.code_number
 #hi this is a test