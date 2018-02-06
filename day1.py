import os

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))][0][0]
instructions += instructions[0]
total = 0
for x in range(len(instructions)-1):
    if instructions[x] == instructions[x+1]:
        total += int(instructions[x])
print(total)
instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))][0][0]
y = len(instructions)/2
instructions += instructions[0:int(y)]
total = 0
for x in range(len(instructions)-int(y)):
    if instructions[x] == instructions[x+int(y)]:
        total += int(instructions[x])
print(total)