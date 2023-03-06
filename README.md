# eightpuzzles-solver

It is a solver for a eight puzzles.
A eight puzzle consists of 8 blocks. 7 out of 8 blocks have a random integer in range (1,7). The only possible action is moving a block to an empty spot.  How the blocks are arranged is called a state. 
A solver takes a randomized state of the puzzle. Its goal is to return it with the numbers reorganized to 1 to 7 in order.
The solver needs to find a way to get to the goal state of the puzzle from its initial state. The solver finds the most efficient way to reorganize the puzzle. 
