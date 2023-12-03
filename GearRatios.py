
import unicodedata
def validateAdjacent(symbolsSet,row,col):
    pos = [f"{row-1,col-1}",f"{row-1,col}",f"{row-1,col+1}",f"{row,col-1}",f"{row,col}",f"{row,col+1}",f"{row+1,col-1}",f"{row+1,col}",f"{row+1,col+1}"]
    for curPos in pos:
        if curPos in symbolsSet:
            #print(curPos)
            return True
    return False



with open("gearratios.txt", "r") as f:
    symbols = set()
    currentline = f.readline()
    size = len(currentline) - 1
    matrix = [['0' for _ in range(size)] for _ in range(size)]
    i = 0
    while i<size:
        k = 0
        for ch in currentline:
            if k < size:
                matrix[i][k] = ch
                if ch != "." and not ch.isdigit():
                    symbols.add(f"{i,k}")
            k+=1
        i+=1
        currentline=f.readline()
    i = 0
    sum = 0
    for line in matrix:
        k = 0
        curnum = "0"
        isValid = False
        for cell in line:
            # if cell.isdigit():
            #     curnum+=cell
            # else: 
            #     sum += int(curnum)
            #     curnum = "0"
            if cell.isdigit() and isValid:
                curnum+=cell
                if k+1==size: 
                    sum += int(curnum)    
            elif cell.isdigit() and not isValid:
                curnum+=cell
                isValid = validateAdjacent(symbols,i,k)
            elif not cell.isdigit() and isValid:
                sum += int(curnum)
                curnum = "0"
                isValid = False
            else:
                curnum = "0"
                isValid = False
            k+=1
        i+=1
    print(sum)
        
                

            
    
    
    