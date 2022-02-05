from pprint import pprint

# some mazes
#maze_str = "*****\n*o*x*\n*   *\n*****"
#maze_str = "*******\n*o    *\n* x****\n*     *\n*******"
#maze_str = "*******\n*o    *\n* x** *\n*     *\n*******"
maze_str = "*******\n*o    *\n*     *\n* x** *\n*******"
#maze_str = "*******\n*o    *\n*  x  *\n*     *\n*******"


# symbols used to describe parts of the maze
WALL = '*'
SPACE = ' '
START = 'x'
END = 'o'

# assign numbers to the directions the 'player' can face, so turning right
# always means adding one, and turning left always means subracting one.
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# give names to the directions, not just numbers
facingName = ("North", "East", "South", "West")


def getMaze(m_str):
    '''
    m_str: string representing the maze as symbols described at the top of the
        code
    returns: 2d list describing the maze
    '''
    maze = []
    line = []

    for ch in maze_str:
        if ch == '\n':
            maze.append(line)
            line = []
        else:
            line.append(ch)
    maze.append(line)
    return maze


def getStartEnd(maze, start):
    '''
    gets the start or end point of a maze
    maze: 2d list describing the maze
    start: bool, True if we want to return the start point, False if we want
        to return the end point
    returns: a tuple with the col and row of the item searched for
    '''
    if start:
        SYMBOL = START
    else:
        SYMBOL = END

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == SYMBOL:
                return (row, col)
    return (0, 0)

def getTestLoc(pos, facing, dir):
    '''
    pos: tuple containing current coordinates of 'player'
    facing: integer representing the direction the 'player' is facing (N,S,E,W)
    dir: string representing the direction we want to know about (forward, left,
    #   right, back)
    returns: tuple contaning the coordinates of the space in the direction we
    #   want relative to the 'player' position and facing.
    '''
    if facing == 0:
        forward = (pos[0]-1, pos[1])
        right = (pos[0], pos[1]+1)
        back = (pos[0]+1, pos[1])
        left = (pos[0], pos[1]-1)
    elif facing == 1:
        left = (pos[0]-1, pos[1])
        forward = (pos[0], pos[1]+1)
        right = (pos[0]+1, pos[1])
        back = (pos[0], pos[1]-1)
    elif facing == 2:
        back = (pos[0]-1, pos[1])
        left = (pos[0], pos[1]+1)
        forward = (pos[0]+1, pos[1])
        right = (pos[0], pos[1]-1)
    elif facing == 3:
        right = (pos[0]-1, pos[1])
        back = (pos[0], pos[1]+1)
        left = (pos[0]+1, pos[1])
        forward = (pos[0], pos[1]-1)

    if dir == "forward":
        return forward
    elif dir == "back":
        return back
    elif dir == "right":
        return right
    elif dir == "left":
        return left


def mainLoop(maze):
    '''
    move the player until they find the exit or the algorithm fails.
    maze: 2d list describing the maze
    start: tuple with col and row of start position
    end: tuple with col and row of end position
    returns: True if the end is found, False if the player returns to the
        start
    '''
    start = getStartEnd(myMaze, True)
    end = getStartEnd(myMaze, False)
    player_pos = start
    player_face = NORTH
    print("Current position: {}".format(player_pos))

    # code to control the player goes here
    while True:
        print("At {} facing {}".format(player_pos, facingName[player_face]))

        checkForward = getTestLoc(player_pos, player_face, "forward")
        checkRight = getTestLoc(player_pos, player_face, "right")
        checkLeft = getTestLoc(player_pos, player_face, "left")
        checkBack = getTestLoc(player_pos, player_face, "back")

        if maze[checkRight[0]][checkRight[1]] != WALL:
            # check if going right will work
            player_pos = checkRight
            player_face = (player_face + 1) % 4
        elif maze[checkForward[0]][checkForward[1]] != WALL:
            # check in going forward will work
            player_pos = checkForward
            player_face = player_face
        elif maze[checkLeft[0]][checkLeft[1]] != WALL:
            # check if going left will work
            player_pos = checkLeft
            player_face = (player_face - 1) % 4
        elif maze[checkBack[0]][checkBack[1]] != WALL:
            # check if going back will work
            player_pos = checkBack
            player_face = (player_face - 2) % 4
        else:
            # maze is broken, return False
            return False

        if player_pos == end:
            print("Exit at {}".format(player_pos))
            return True
        if player_pos == start:
            return False


def printMaze(maze):
    '''
    maze: 2d list representing the maze.
    output: prints the maze to the screen.
    '''
    for line in maze:
        print(''.join(line))


if __name__ == '__main__':
    myMaze = getMaze(maze_str)  # maze data structure from str representation
    printMaze(myMaze)           # print maze to screen
    mazeRun = mainLoop(myMaze)  # run the main loop
    if mazeRun:
        print("Success!")       # exit found
    else:
        print("Failure!")       # 'player' came back to start
