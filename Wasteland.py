import re

with open("wasteland.txt", "r") as f:
    instructions = f.readline().strip()
    mapCoordinates = {}
    
    for line in f.readlines():
        if len(line.strip())==0:
            continue
        strs = re.findall(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
        mapCoordinates.update({strs[0][0]:[strs[0][1],strs[0][2]]})
    
    currentPoint = "AAA"
    currentInstruction = 0
    steps = 0
    found = False
    while not found:
        if currentPoint == "ZZZ":
            found = True
        else: 
            instruction = instructions[currentInstruction]
            if instruction == "L":
                currentPoint=mapCoordinates.get(currentPoint)[0]
            else: 
                currentPoint=mapCoordinates.get(currentPoint)[1]
            currentInstruction += 1
            if currentInstruction == len(instructions):
                currentInstruction = 0            
            steps +=1
    print(steps)

    
    
