with open("scratchcards.txt", "r") as f:
    data = f.readlines()
    sumPoints = 0
    instances = [1]*len(data)
    currentGame = 0
    for line in data: 
        winners = line[line.find(':')+1:line.find('|')].split(" ")
        mycards = line[line.find('|')+1:].strip().split(" ")
        numWinners = 1
        for winner in winners:
            if winner!='':
                try: 
                    #Check if the current winner is in my cards
                    mycards.index(winner)                
                    #If it is I add the ammount of my instances to the next winning card index
                    instances[currentGame+numWinners]+=instances[currentGame]
                    numWinners+=1
                except ValueError:
                    ValueError.args
        #Add the current game's instances to the points
        sumPoints+=instances[currentGame]
        currentGame+=1
    print(sumPoints)