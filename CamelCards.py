import re

cardvalues = {"A":14,"K":13,"Q":12,"J":1,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

with open("camelcards.txt", "r") as f:
    games = f.readlines();    
    scores = []
    for game in games:
        level = 1        
        cardsBet = game.split()        
        numJs = cardsBet[0].count("J")
        tups5 = re.findall(r"(.)(?=(.*\1){4})", cardsBet[0])
        tups4 = re.findall(r"(.)(?=(.*\1){3})", cardsBet[0])        
        tups3 = re.findall(r"(.)(?=(.*\1){2})", cardsBet[0])
        tups2 = [char for char in set(cardsBet[0]) if len(re.findall(char, cardsBet[0])) == 2]
        if len(tups5) == 1:
            level = 7
        elif len(tups4) == 1:
            if numJs == 1 or numJs == 4:
                level = 7
            else:
                level = 6
        elif len(tups3) == 1 and  len(tups2) == 1:
            if numJs >= 2:
                level = 7
            else: 
                level = 5
        elif len(tups3) == 1 and  len(tups2) == 0:
            if numJs == 1 or numJs == 3:
                level = 6
            else:
                level = 4
        elif len(tups2) == 2:
            if numJs == 1:
                level = 5
            elif numJs == 2:
                level = 6
            else:
                level = 3
        elif len(tups2) == 1:
            if numJs == 1 or numJs == 2:
                level = 4            
            else:
                level = 2
        else:
            if numJs == 1:
                level = 2

    
        scores.append((level,
                       cardvalues.get(cardsBet[0][0]),
                       cardvalues.get(cardsBet[0][1]),
                       cardvalues.get(cardsBet[0][2]),
                       cardvalues.get(cardsBet[0][3]),
                       cardvalues.get(cardsBet[0][4]),
                       cardsBet[1]))
    scores.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
    print(scores)
    totalScore = 0
    for i, s in enumerate(scores):
        totalScore += (i+1)*int(s[6])
    print(totalScore)
    