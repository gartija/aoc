import re, numpy

def calculateSteps(currentPoint,instructions,mapCoordinates)-> int: 
    #currentPoint = "AAA"
    currentInstruction = 0
    steps = 0
    found = False
    while not found:
        if currentPoint[2] == "Z":
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
    return steps

with open("wasteland.txt", "r") as f:
    instructions = f.readline().strip()
    mapCoordinates = {}
    startingCoordinates = []
    
    for line in f.readlines():
        if len(line.strip())==0:
            continue
        strs = re.findall(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
        mapCoordinates.update({strs[0][0]:[strs[0][1],strs[0][2]]})
        start = re.findall(r"([A-Z]{2}A) = \([A-Z]{3}, [A-Z]{3}\)", line)
        if len(start)==1:
            startingCoordinates.append(start[0])

    lcm = 1
    for k in startingCoordinates:
        steps = calculateSteps(k,instructions,mapCoordinates)
        lcm = numpy.lcm(steps,lcm)
    print(lcm)


    

    
    
