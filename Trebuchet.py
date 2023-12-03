
with open("trebuchet.txt", "r") as f:
    data = f.readlines()
    sum = 0 
    map = dict({"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"})
    for line in data:
        min = [len(line)+1,0]
        max = [-1,0]
        for key in map:
            lf = line.find(key)
            rf = line.rfind(key)
            if lf > -1 and lf<min[0]:
                min[0] = lf
                min[1] = map[key]
            if rf > -1 and rf>max[0]:
                max[0] = rf
                max[1] = map[key]
        sum+= int(min[1]+max[1])
    print(sum)



