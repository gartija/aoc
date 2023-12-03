import re

def possible(input_string,map)->(int,bool): 
#Pattern to extract the game ID
    pattern = r"Game (\d*)"
    match = re.findall(pattern,input_string)
    game = int(match[0])
    pattern = r"(?P<color>[0-9]+)[ \t]+\b(?P<amount>blue|green|red)\b"
    match = re.findall(pattern, input_string)
    if match:
        # Print the results
        for group in match:
            color = group[1]
            amount = int(group[0])
            if map[color]<amount:
                #print(f"Not possible {amount} {color} Game: {game}")
                return (game,False)
    else:
        print("No match found.")
    return (game,True)

def power(input_string)->int:
    pattern = r"(?P<color>[0-9]+)[ \t]+\b(?P<amount>blue|green|red)\b"
    match = re.findall(pattern, input_string)
    map = dict({})
    if match:
        # Print the results
        for group in match:
            color = group[1]
            amount = int(group[0])
            currentAmount = map.get(color)
            if currentAmount is None or currentAmount < amount:
                map.update({color:amount})
    else:
        print("No match found.")
    ret = 1
    for v in map.values():
        ret*=v
    return ret


map = dict({"red":12, "green":13,"blue":14})
with open("cubeconundrum.txt", "r") as f:
    data = f.readlines()
    sum = 0
    for line in data:
        sum+=power(line)
        #print(line)
        #pos = possible(line,map)
        #if pos[1] is True:
        #    sum+=pos[0]
    print(sum)


