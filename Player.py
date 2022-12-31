#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player():
    def __init__(self, checker):
        """ Constructs a new Player object by initializing two 
            attributes.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ Returns a string representing a Player object. The string returned
            should indicate which checker the Player object is using.
        """
        s = "Player "
        s += self.checker
        return s
    
    def opponent_checker(self):
        """ Returns a one-character string representing the checker of the Player 
            object’s opponent. The method may assume that the calling Player 
            object has a checker attribute that is either 'X' or 'O'.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ Accepts a Board object b as a parameter and returns the column 
            where the player wants to make the next move.
        """
        column = int(input("Enter a column: "))
        wrongInput = True
        while wrongInput:
            if b.can_add_to(column) == False:
                print("Try again!")
                print()
                column = int(input("Enter a column: "))
            else:
                self.num_moves += 1
                return column
        return self.num_moves
        
        
