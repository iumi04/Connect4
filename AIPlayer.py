from proj import *
import random  

class AIPlayer(Player):
    """ Look ahead some number of moves into the future to assess the impact of
        each possible move that it could make for its next move, and it will assign 
        a score to each possible move. And since each move corresponds to a column
        number, it will effectively assign a score to each column.
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ Constructs a new AIPlayer object.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ Returns a string representing an AIPlayer object. This method will 
            override/replace the __repr__ method that is inherited from Player.
            In addition to indicating which checker the AIPlayer object is using,
            the returned string should also indicate the player’s tiebreaking
            strategy and lookahead.
        """
        s = "Player "
        s += self.checker
        s += " (" + self.tiebreak + ", "
        s += str(self.lookahead) + ")"

        
        return s
    
    def max_score_column(self, scores):
        """ Takes a list scores containing a score for each column of the board 
            and returns the index of the column with the maximum score. If one
            or more columns are tied for the maximum score, the method should 
            apply the called AIPlayer‘s tiebreaking strategy to break the tie.
        """
        value = max(scores)
        list = []
        for i in range(len(scores)):
            if scores[i] == value:
                list += [i]
        if self.tiebreak == 'LEFT':
            return list[0]
        elif self.tiebreak == 'RIGHT':
            return list[-1]
        else:
            return random.choice(list)
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores
            for the columns in b.
        """
        scores = [50] * b.width
        for i in range(b.width):
            if not(b.can_add_to(i)):
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50  
            else:
                b.add_checker(self.checker,i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
        
                if max(opp_scores) == 100:
                    scores[i] = 0
                elif max(opp_scores) == 50:
                    scores[i] = 50
                elif max(opp_scores) == 0:
                    scores[i] = 100
                else:
                    scores[i] = -1
                b.remove_checker(i)
        
        return scores
    
    def next_move(self, b):
        """ Overrides (i.e., replaces) the next_move method that is inherited from
            Player. Rather than asking the user for the next move, this version
            of next_move should return the called AIPlayer‘s judgment of its best
            possible move.
        """
        best_move = self.max_score_column(self.scores_for(b))
        self.num_moves += 1
        return best_move
