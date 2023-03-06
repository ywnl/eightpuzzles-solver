#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Jasper Hoong
# email: jasperh@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Yewon Lee
# partner's email:ywnl@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """Constructs a new Searcher object by initializing states, num_tested, and depth_limit"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """Takes a single State object called new_state and adds it to the Searcher‘s list of untested states."""
        self.states += [new_state]
        
    def should_add(self, state):
        """Takes a State object called state and returns True if the called Searcher 
        should add state to its list of untested states, and False otherwise."""
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle():
            return False
        return True
            
    def add_states(self, new_states):
        """Takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time to determine if they should be added
        to the list states"""
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """Performs a full state-space search that begins at the specified initial 
        state init_state and ends when the goal state is found or when the Searcher 
        runs out of untested states."""
        self.add_state(init_state)
        while len(self.states) != 0:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None # failure
    
    

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ A class for objects that perform a Breadth-first search on an Eight Puzzle.
    """
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """ A class for objects that perform a Depth-first search on an Eight Puzzle.
    """
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = self.states[-1]
        self.states.remove(s)
        return s
    
    
def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ a heuristic function that returns estimate of how many moves left"""
    return state.board.num_misplaced()

def h2(state):
    """ a heuristic function that returns estimate of how many moves left"""
    count = 0
    #check for if there is anything that is either in wrong row or column and use that to give score count twice for both wrong" once for onc"e wrong
    for row in range(len(state.board.tiles)):
        for col in range(len(state.board.tiles[0])):
            if state.board.tiles[row][col] in '012' and row != 0:
                count +=1
            if state.board.tiles[row][col] in '036' and col != 0:
                count +=1
            if state.board.tiles[row][col] in '345' and row != 1:
                count +=1
            if state.board.tiles[row][col] in '147' and col != 1:
                count +=1
            if state.board.tiles[row][col] in '678' and row != 2:
                count +=1
            if state.board.tiles[row][col] in '258' and col != 2:
                count+=1
          
    return count
    
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """initializes GreedySearcher class
        """
        super().__init__(heuristic)
        self.depth_limit = -1
        self.heuristic = heuristic
    
    def add_state(self, state):
        """Takes a state and adds it to the list of untested states
        """
        self.states += [[self.priority(state),state]]
        
    def next_state(self):
        """choose next state with highest priority from the list of untested states, 
        removing it from the list and returning it

        """
        s = max(self.states)
        self.states.remove(s)
        return s[1]

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

### Add your AStarSeacher class definition below. ###
class AStarSearcher(Searcher):
    """A class for objects that performs an informed A* search on an eight-puzzle
    """
    def __init__(self, heuristic):
        """initializes AStarSearcher class
        """
        super().__init__(heuristic)
        self.depth_limit = -1
        self.heuristic = heuristic
        
    def add_state(self, state):
        """Takes a state and adds it to the list of untested states
        """
        self.states += [[self.priority(state),state]]
        
    def next_state(self):
        """choose next state with highest priority from the list of untested states, 
        removing it from the list and returning it

        """
        s = max(self.states)
        self.states.remove(s)
        return s[1]
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function and num_moves used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
