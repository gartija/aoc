
with open("trebuchet.txt", "r") as f:
    data = f.readlines()
    sum = 0 
    for line in data:
        first = None
        last = None
        for currentDigit in line:
            if currentDigit.isnumeric() and first is None:
                first = currentDigit
            if currentDigit.isnumeric():
                last = currentDigit
        #if last is None:
        #    last = first
        sum+= int(first+last)
    print(sum)



