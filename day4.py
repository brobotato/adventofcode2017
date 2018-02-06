import os,functools

def combine(list):
    return functools.reduce(lambda x,y:x+y,list)

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))]
for l in instructions:
    temp = {}
    for x in l:
        if x in temp:
            temp[x] += 1
        else:
            temp[x] = 1
    instructions[instructions.index(l)] = temp
total = 0
for x in instructions:
    lol = [x[key] for key in x]
    if lol == [1]*len(lol):
        total += 1
print(total)

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))]
for l in instructions:
    temp = {}
    for y in l:
        ha = sorted(y)
        x = combine(ha)
        if x in temp:
            temp[x] += 1
        else:
            temp[x] = 1
    instructions[instructions.index(l)] = temp
total = 0
for x in instructions:
    lol = [x[key] for key in x]
    if lol == [1]*len(lol):
        total += 1
print(total)