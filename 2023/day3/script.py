import re
from itertools import product

with open("input.txt", "r") as txtFile:
    txtRead = txtFile.read()
    total = sum([eval(i) for i in re.findall(r'\d+' , txtRead)])
    print(total)
    grid = txtRead.split()
    for line in range(len(grid)):
        grid[line] = "a" + grid[line]
        grid[line] = grid[line]  + 'a'

    grid.insert(0, 'a' * len(grid[0]))
    grid.append('a' * len(grid[0]))        
    numStrings = ""
    for y in range(len(grid)):
        flag = False
        for x in range(len(grid[y])):
            if grid[y][x].isnumeric():
    
                coord = product([0, 1, -1], repeat=2)

                for pos in coord:
                    posCheck = grid[y + pos[0]][x + pos[1]] 

                    #if special char found, empty out numStrings
                    if not posCheck.isalnum() and posCheck != ".":
                        flag = True
                #otherwise keep adding the number
                if flag == False:
                    numStrings = numStrings + grid[y][x]
                else:
                    numStrings = ""
            else:
                if numStrings:
                    print(numStrings)
                    total -= int(numStrings)
                #hard reset once we reach the end
                numStrings = ""
                flag = False
print(total)
