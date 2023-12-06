
seeds = [4106085912,135215567,529248892,159537194,1281459911,114322341,1857095529,814584370,2999858074,50388481,3362084117,37744902,3471634344,240133599,3737494864,346615684,1585884643,142273098,917169654,286257440]

with open("seedfertilizer.txt", "r") as f:
    data = f.readlines()
    maps = []
    #Although it's redundant I map the file contents into a map (actually it's an 3D matrix)
    for line in data:
        if line.find(":")!= -1:
            maps.append([])
        else: 
            currentLine = line.strip().split(" ")
            if len(currentLine) == 3:
                ar = [int(currentLine[0]),int(currentLine[1]),int(currentLine[2])]
                maps[len(maps)-1].append(ar)
    
    lowestLocation = None
    #Iterate though the seeds 
    for seedVal in seeds:
        currentLocation = 0
        sourcevalue = seedVal
        #Iterate through the xTox mappings
        for xTox in maps:
            newSourceValue = -1
        #Iterate through each xTox to find if the current 
            for currentMapping in xTox:
                if sourcevalue>=currentMapping[1] and sourcevalue<=currentMapping[1]+currentMapping[2]:
                    newSourceValue = currentMapping[0] + sourcevalue - currentMapping[1]
                    #I should exit loop here
            if newSourceValue != -1:
                sourcevalue =newSourceValue
        if lowestLocation is None or sourcevalue< lowestLocation:
            lowestLocation = sourcevalue
    print(lowestLocation)

            


    #print(maps)

        

    