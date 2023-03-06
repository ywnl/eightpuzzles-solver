#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Jasper Hoong
# email: jasperh@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Yewon Lee
# partner's email:ywnl@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        num = 0
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j] = digitstr[num]
                num += 1
                if self.tiles[i][j] == '0':
                    self.blank_r = i
                    self.blank_c = j


    ### Add your other method definitions below. ###

    def __repr__(self):
        """returns a string representation of a Board object"""
        s = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] == '0':
                    s+= '_ '
                else:
                    s+= self.tiles[i][j] + ' '
            s+= '\n'
        return s
    
    def move_blank(self, direction):
        """Takes an input and a string direction that specifies the direction 
        in which the blank should move, and that attempts to modify the 
        contents of the called Board object accordingly.
        The method should return True or False to indicate whether 
        the requested move was possible.
        """
        row = 0
        col = 0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] == '0':
                    row = i
                    col = j
                    
        if direction == 'down':
            if row == 2:  
                return False
            else:
                self.tiles[row][col] = self.tiles[row+1][col]
                self.tiles[row+1][col] = '0'
                self.blank_r = row+1
                return True
        elif direction == 'right':
            if col == 2:
                return False
            else:
                self.tiles[row][col] = self.tiles[row][col+1]
                self.tiles[row][col+1] = '0'
                self.blank_c = col+1
                return True
        elif direction == 'up':
            if row == 0:
                return False
            else:
                self.tiles[row][col] = self.tiles[row-1][col]
                self.tiles[row-1][col] = '0'
                self.blank_r = row-1
                return True
        elif direction == 'left':
            if col == 0:
                return False
            else:
                self.tiles[row][col] = self.tiles[row][col-1]
                self.tiles[row][col-1] = '0'
                self.blank_c = col-1
                return True
        
    def digit_string(self):
        """Creates and returns a string of digits that corresponds to the current contents of the called Board object’s tiles attribute."""
        s = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                s+=self.tiles[i][j]
        return s

    def copy(self):
        """Returns a newly-constructed Board object that is a deep copy of 
        the called object"""
        b = Board(self.digit_string())
        return b
    
    def num_misplaced(self):
        """Counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state."""
        count = 0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] != GOAL_TILES[i][j]:
                    count += 1
        return count-1
    
    def __eq__(self, other):
        """Called when the == operator is used to compare two Board objects. """
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] != other.tiles[i][j]:
                    return False
        return True