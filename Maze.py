import Viewer

EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4
    
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

if __name__ == "__main__":
    grid = [
        [ WALL,  WALL,  EMPTY,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL, WALL],
        [START, EMPTY,  WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  EMPTY, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY,  WALL, WALL],
        [ WALL,  WALL,  WALL,  WALL, EMPTY,  WALL, WALL,  WALL, EMPTY, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY, EMPTY, EMPTY, WALL],
        [ WALL,  WALL, EMPTY,  WALL,  WALL, EMPTY, WALL,  WALL, EMPTY, WALL],
        [ WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL,  EMPTY, EMPTY,  END],
        [ WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL, WALL],
    ]
                    
    Viewer.view(grid)


    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    currentRow = 1
    currentCol = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(currentRow) + ", " + str(currentCol) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            currentRow -= 1
            
        elif direction == EAST:
            currentCol += 1
                
        elif direction == SOUTH:
            currentRow += 1
                
        elif direction == WEST:
            currentCol -= 1
        
        else:
            print("You have no idea where you'are going") # Invalid direction.
        
        if (currentRow < 0 or currentCol < 0 
                        or currentRow >= len(grid) 
                        or currentCol >= len(grid[currentRow])):
            done = True
            print("You fall into the chasm of doom") # Out of bounds.
            
        else:

            cell = grid[Row][Col]
        
            if cell == EMPTY:
                 grid[Row][Col] == VISITED
                
            elif cell == WALL:
                done = True
                print("You stumble blindly into a solid concrete wall") # Hit wall.

            elif cell == END:

                solved = True
                print("Solved") # Solved.
                
            else:
                pass # Do nothing
    
        
        charIndex += 1
    # end-while


    if not solved:
        print("You have fail to escape, Future archeologogist gaze upon your remains in the bafflement") # Did not reach the end.


    Viewer.view(grid)
