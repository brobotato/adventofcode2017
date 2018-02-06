import os,functools

def combine(list):
    return functools.reduce(lambda x,y:x+y,list)

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))][0]
instructions = [int(x) for x in instructions]

history = []
steps = 0

while instructions not in history:
    steps += 1
    history.append([x for x in instructions])
    a = max(instructions)
    b = instructions.index(max(instructions))
    instructions[b] = 0
    for x in range(a):
        instructions[(b+1+x)%len(instructions)] += 1
print(steps)
print(steps-history.index(instructions))