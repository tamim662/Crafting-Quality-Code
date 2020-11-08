# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:

    """ A rat caught in a maze. """
    def __init__(self,symbol,row, col,num_sprouts_eaten=0):
        self.symbol=symbol
        self.row=row
        self.col=col
        self.num_sprouts_eaten=num_sprouts_eaten
    
    def set_location(self,row,col):
        self.row=row
        self.col=col
        
    
    def eat_sprout(self):
        self.num_sprouts_eaten+=1

    def __str__(self):
        # symbol at (row, col) ate num_sprouts_eaten sprouts.
        result="{0} at ({1},{2}) ate {3} sprouts".format(self.symbol,self.row,self.col,self.num_sprouts_eaten)
        return result
        


    # Write your Rat methods here.

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self,maze,rat_1,rat_2):
        self.maze=maze
        self.rat_1=rat_1
        self.rat_2=rat_2

        count = 0
        for i in range(0, len(maze)):
            for j in range(0, len(maze[0])):
                if self.maze[i][j] == SPROUT:
                    count += 1
        self.num_sprouts_left=count
    

    def is_wall(self,row,col):
        return self.maze[row][col]== WALL

    def get_character(self,row,col):
        
        char = self.maze[row][col]
        if (self.rat_1.row,self.rat_1.col) == ( row, col ):
            char = self.rat_1.symbol
        elif (self.rat_2.row,self.rat_2.col) == ( row, col ):
            char = self.rat_2.symbol
        return char
    
    def move(self,Rat,ver_change, hor_change):
        new_location = ( Rat.row + ver_change, Rat.col + hor_change )
        elem = self.get_character( new_location[0], new_location[1] )
        if elem == WALL:
            return False
        else:
            Rat.set_location(new_location[0], new_location[1] )
            if elem == SPROUT:
                Rat.eat_sprout()
                self.maze[new_location[0]][new_location[1]]= HALL
                self.num_sprouts_left -= 1
            return True

    def __str__(self):
        self.maze[self.rat_1.row][self.rat_1.col] = RAT_1_CHAR
        self.maze[self.rat_2.row][self.rat_2.col] = RAT_2_CHAR

        maze_string = ""
        for row in self.maze:
            for c in row:
                maze_string += str(c)
            maze_string += "\n"

        maze_string = maze_string[:-1]

        return "{0}\n{1}.\n{2}.".format(str(maze_string), str(self.rat_1), str(self.rat_2))
