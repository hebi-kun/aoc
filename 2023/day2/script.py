import re

with open("input.txt") as txtFile:
    readFile = txtFile.read().split("\n")
    
    total = 0 
    
    totalMax = 0
    for line in readFile:
        line.replace(";", " ")
        game = re.search(r"\d+", line)
        game = int(game.group()) if game else 0
        
        redLimit = 12
        greenLimit = 13
        blueLimit = 14
        
        redCheck = True 
        blueCheck = True 
        greenCheck = True
        
        redNumbers =[eval(i) for i in re.findall(r"(\d+) red", line)]
        blueNumbers = [eval(i) for i in re.findall(r"(\d+) blue", line)]
        greenNumbers = [eval(i) for i in re.findall(r"(\d+) green", line)]
        print(redNumbers)
        print(blueNumbers)
        print(greenNumbers, "----------")
        maxRed = max(redNumbers) if redNumbers else 0
        maxBlue = max(blueNumbers) if blueNumbers else 0
        maxGreen = max(greenNumbers) if greenNumbers else 0
        
        totalMax += (maxRed * maxBlue * maxGreen)

        for i in redNumbers: 
            if i > redLimit:
                redCheck = None
        for i in blueNumbers:
            if i > blueLimit:
                blueCheck = None
        for i in greenNumbers:
            if i > greenLimit:
                greenCheck = None

        

        if redCheck and greenCheck and blueCheck and game != 0:
            total += game
        else:
            print("Game", game, "not possible")
    print(total)
    print(totalMax)    
