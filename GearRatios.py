
import unicodedata
def validateAdjacent(symbolsMap,row,col):
    pos = [f"{row-1,col-1}",f"{row-1,col}",f"{row-1,col+1}",f"{row,col-1}",f"{row,col}",f"{row,col+1}",f"{row+1,col-1}",f"{row+1,col}",f"{row+1,col+1}"]
    for curPos in pos:
        if curPos in symbolsMap:
            return curPos
    return None



with open("gearratios.txt", "r") as f:
    symbols = dict({})
    currentline = f.readline()
    size = len(currentline) - 1
    matrix = [['0' for _ in range(size)] for _ in range(size)]
    i = 0
    while i<size:
        k = 0
        for ch in currentline:
            if k < size:
                matrix[i][k] = ch
                if ch == "*":
                    symbols.update({f"{i,k}":0})
            k+=1
        i+=1
        currentline=f.readline()
    i = 0
    sum = 0
    for line in matrix:
        k = 0
        curnum = "0"
        gearPos = None
        for cell in line:
            if cell.isdigit() and gearPos is not None:
                curnum+=cell
                if k+1==size: 
                    if symbols.get(gearPos) == 0:
                        symbols.update({gearPos:int(curnum)}) 
                    else:
                        sum += int(curnum)*symbols.get(gearPos)
            elif cell.isdigit() and gearPos is None:
                curnum+=cell
                gearPos = validateAdjacent(symbols,i,k)
            elif not cell.isdigit() and gearPos is not None:
                if symbols.get(gearPos) == 0:
                    symbols.update({gearPos:int(curnum)}) 
                else:
                    sum += int(curnum)*symbols.get(gearPos)
                curnum = "0"
                gearPos = None
            else:
                curnum = "0"
                gearPos = None
            k+=1
        i+=1
    print(sum)
        
                

            
    
    
    