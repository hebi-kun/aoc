with open("input.txt", "r") as txtFile:
    fileRead = txtFile.read()

    total = 0

    numDict = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
    
    for k , v in numDict.items():
        fileRead = fileRead.replace(k, v)
    
    for line in fileRead.split():
        left, right = 0, len(line) - 1
        numString = ""
        
        while left <= right:
            if line[left].isnumeric() and line[right].isnumeric():
                numString += line[left] + line[right]
                break
            
            if line[left].isalpha():
                left += 1

            if line[right].isalpha():
                right -= 1
        if len(numString) == 2:
            total += int(numString)
            continue   
    print(total)

