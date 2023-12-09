
def extrapolate(arr) -> int:
    newarr = []
    previousValue = arr[0] 
    allZeroes = True
    for item in arr[1:]:
        newarr.append(item - previousValue)
        if (item - previousValue)!=0:
            allZeroes = False
        previousValue = item
    if allZeroes:
        return arr[len(arr)-1]
    else: 
        return arr[len(arr)-1]+extrapolate(newarr)

with open("miragemaintenance.txt", "r") as f:
    lines = f.readlines()
    extrapolated = 0
    for line in lines:        
        arrNums = [int(x) for x in line.strip().split(" ")]
        extrapolated += extrapolate(arrNums)
    print(extrapolated)