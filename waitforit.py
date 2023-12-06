
time = [49787980]
distance = [298118510661181]
totalNWays = 1

for j, t in enumerate(time): 
    nWays = 0
    for i in range(1,t):
        if (t-i)*i>distance[j]:
            nWays+=1
            #print((t-i)*i)
    totalNWays*=nWays
    j+=1
print(totalNWays)