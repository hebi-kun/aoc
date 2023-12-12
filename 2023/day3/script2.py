import re
from itertools import product

with open("input.txt", "r") as txtFile:
    txtRead = txtFile.read()
    grid = txtRead.split()
    for line in range(len(grid)):
        grid[line] = "a" + grid[line]
        grid[line] = grid[line]  + 'a'

    grid.insert(0, 'a' * len(grid[0]))
    grid.append('a' * len(grid[0]))        
    numStrings = ""
    
    total = 0

    gearDict = {}
    for y in range(len(grid)):
        starPos = ()
        for x in range(len(grid[y])):
            if grid[y][x].isnumeric():
                
                coord = product([0, 1, -1], repeat=2)

                for pos in coord:
                    posCoord = (y + pos[0], x + pos[1])
                    posVal = grid[y + pos[0]][x + pos[1]] 

                    if posVal == "*": 
                        if posCoord not in gearDict.keys():
                            gearDict[(y + pos[0], x + pos[1])] = [] 
                            starPos = posCoord
                        else:
                            starPos = posCoord

                numStrings = numStrings + grid[y][x]
                
            else:

                if starPos:
                    gearDict[starPos].append(int(numStrings))
                #hard reset once we reach the end
                starFound = False
                starPos = ()
                numStrings = ""
    
    for value in gearDict.values():
        if len(value) > 1:
            total += (value[0] * value[1])
    print(total)
