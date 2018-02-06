import os

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))]
total = 0
for l in instructions:
    instructions[instructions.index(l)] = [int(x) for x in l]
for l in instructions:
    total += max(l)-min(l)
print(total)
total = 0
for l in instructions:
    for x in l:
        for y in l[l.index(x)+1:]:
            if(x%y==0):
                print(x,y)
                total += x/y
            if(y%x==0):
                print(y,x)
                total += y/x
print(total)