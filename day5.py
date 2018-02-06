import os,functools

def combine(list):
    return functools.reduce(lambda x,y:x+y,list)

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))]
instructions = combine(instructions)
instructions = [int(x) for x in instructions]

x = 0
steps = 0
while x>=0 and x<len(instructions):
    instructions[x] += 1
    steps += 1
    x += instructions[x] - 1
print(steps)

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))]
instructions = combine(instructions)
instructions = [int(x) for x in instructions]

x = 0
steps = 0
while x>=0 and x<len(instructions):
    if instructions[x] >= 3:
        instructions[x] -= 1
        steps += 1
        x += instructions[x] + 1
    else:
        instructions[x] += 1
        steps += 1
        x += instructions[x] - 1
print(instructions)
print(steps)