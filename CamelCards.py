import re

cardvalues = {"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

with open("camelcards.txt", "r") as f:
    games = f.readlines();    
    scores = []
    for game in games:
        cardsBet = game.split()        
        tups5 = re.findall(r"(.)(?=(.*\1){4})", cardsBet[0])
        tups4 = re.findall(r"(.)(?=(.*\1){3})", cardsBet[0])        
        tups3 = re.findall(r"(.)(?=(.*\1){2})", cardsBet[0])
        tups2 = [char for char in set(cardsBet[0]) if len(re.findall(char, cardsBet[0])) == 2]       
        if len(tups5) == 1:
            scores.append((7,cardvalues.get(tups5[0][0]),0,0,0,0,cardsBet[1]))
        elif len(tups4) == 1:
            others=cardsBet[0].replace(tups4[0][0],"")
            scores.append((6,
                           cardvalues.get(tups4[0][0]),
                           cardvalues.get(others[0]),
                           0,
                           0,
                           0,
                           cardsBet[1]))
        elif len(tups3) == 1 and  len(tups2) == 1:
            scores.append((5,cardvalues.get(tups3[0][0]),cardvalues.get(tups2[0]),0,0,0,cardsBet[1]))
        elif len(tups3) == 1 and  len(tups2) == 0:
            others=cardsBet[0].replace(tups3[0][0],"")
            other1 = cardvalues.get(others[0])
            other2 = cardvalues.get(others[1])
            if other2 > other1:
                t = other1
                other1 = other2
                other2 = t
            scores.append((4,
                           cardvalues.get(tups3[0][0]),
                           other1,
                           other2,
                           0,
                           0,
                           cardsBet[1]))
        elif len(tups2) == 2:
            other = cardvalues.get(cardsBet[0].replace(tups2[0],"").replace(tups2[1],""))
            pair1 = cardvalues.get(tups2[0])
            pair2 = cardvalues.get(tups2[1])
            if pair2>pair1:
                t = pair1
                pair1 = pair2
                pair1 = t
            scores.append((3,
                           pair1,
                           pair2,
                           other,
                           0,
                           0,
                           cardsBet[1]))
        elif len(tups2) == 1:
            others=[]
            for other in cardsBet[0].replace(tups2[0],""):
                others.append(cardvalues.get(other))
            others.sort(reverse=True)
            scores.append((2,
                           cardvalues.get(tups2[0]),
                           others[0],
                           others[1],
                           others[2],
                           0,
                           cardsBet[1]))
        else:
            others=[]
            for other in cardsBet[0]:
                others.append(cardvalues.get(other))
            others.sort(reverse=True) 
            scores.append((1,
                           others[0],
                           others[1],
                           others[2],
                           others[3],
                           others[4],
                           cardsBet[1]))
    scores.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))
    totalScore = 0
    for i, s in enumerate(scores):
        totalScore += (i+1)*int(s[6])
        print(i)
        print(s)
        print(totalScore)
    print(totalScore)
    