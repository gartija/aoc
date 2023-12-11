
import sys

def validateUp(cCoord,maze) -> []:
    if cCoord[0]>=1 and (maze[cCoord[0]-1][cCoord[1]]=="|" or maze[cCoord[0]-1][cCoord[1]]=="F" or maze[cCoord[0]-1][cCoord[1]]=="7"):
        return [cCoord[0]-1,cCoord[1]]
    else:
        return None

def validateDown(cCoord,maze) -> []:
    if cCoord[0]<len(maze)-1 and (maze[cCoord[0]+1][cCoord[1]]=="|" or maze[cCoord[0]+1][cCoord[1]]=="J" or maze[cCoord[0]+1][cCoord[1]]=="L"):
        return [cCoord[0]+1,cCoord[1]]
    else:
        return None

def validateRight(cCoord,maze) -> []:
    if cCoord[1]<len(maze[0])-1 and (maze[cCoord[0]][cCoord[1]+1]=="-" or maze[cCoord[0]][cCoord[1]+1]=="J" or maze[cCoord[0]][cCoord[1]+1]=="7"):
        return [cCoord[0],cCoord[1]+1]
    else:
        return None

def validateLeft(cCoord,maze) -> []:
    if cCoord[1]>=1 and (maze[cCoord[0]][cCoord[1]-1]=="-" or maze[cCoord[0]][cCoord[1]-1]=="L" or maze[cCoord[0]][cCoord[1]-1]=="F"):
            return [cCoord[0],cCoord[1]-1]
    else:
         return None

def getNextMoves(currentCoord,maze) -> []:
    currentPipe = maze[currentCoord[0]][currentCoord[1]]
    nextCoords = []    
    up = validateUp(currentCoord,maze)
    down = validateDown(currentCoord,maze)
    left = validateLeft(currentCoord,maze)
    right = validateRight(currentCoord,maze)
    if currentPipe == "S":
        if up is not None:
            nextCoords.append(up)
        if down is not None:
            nextCoords.append(down)
        if right is not None:
            nextCoords.append(right)
        if left is not None:
            nextCoords.append(left)    
    elif currentPipe == "|":
        if up is not None:
            nextCoords.append(up)
        if down is not None:
            nextCoords.append(down)        
    elif currentPipe == "F":
        if right is not None:
            nextCoords.append(right)
        if down is not None:
            nextCoords.append(down)
    elif currentPipe == "L":
        if right is not None:
            nextCoords.append(right)
        if up is not None:
            nextCoords.append(up)
    elif currentPipe == "7":
        if left is not None:
            nextCoords.append(left)
        if down is not None:
            nextCoords.append(down)
    elif currentPipe == "J":
        if up is not None:
            nextCoords.append(up)
        if left is not None:
            nextCoords.append(left)            
    elif currentPipe == "-":
        if left is not None:
            nextCoords.append(left)
        if right is not None:
            nextCoords.append(right)   
    maze[currentCoord[0]][currentCoord[1]] = "x"
    return nextCoords

with open("pipemaze.txt", "r") as f:
    maze = []
    lines = f.readlines()
    sCoord = None
    
    for l, line in enumerate(lines):
        maze.append(list(line.strip()))
        s = line.find("S")
        if  s != -1:
            sCoord = (l,s)

    found = False
    steps = 0
    nMoves = getNextMoves([sCoord[0],sCoord[1]],maze)
    while not found:
        if len(nMoves)==0:
            found = True
        else:
            move = nMoves.pop()
            steps += 1
            moves = getNextMoves([move[0],move[1]],maze)
            for m in moves: 
                nMoves.append(m)
    print(steps/2)
