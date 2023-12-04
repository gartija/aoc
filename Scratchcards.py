with open("scratchcards.txt", "r") as f:
    data = f.readlines()
    sumPoints = 0
    for line in data: 
        winners = line[line.find(':')+1:line.find('|')].split(" ")
        mycards = line[line.find('|')+1:].strip().split(" ")
        currentPointCount = 0
        for winner in winners:
            if winner!='':
                try: 
                    mycards.index(winner)
                    if currentPointCount == 0:
                        currentPointCount = 1
                    else:
                        currentPointCount*=2
                except ValueError:
                    print("Not found")
        sumPoints+=currentPointCount
    print(sumPoints)