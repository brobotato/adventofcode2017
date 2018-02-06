import os, functools


def combine(list):
    return functools.reduce(lambda x, y: x + y, list)


def leaf_price(program):
    if program not in leaves_dict:
        return int(instructions[discs.index(program)][1][1:-1])
    else:
        if program in calculated:
            return calculated[program]
        else:
            total = 0
            total += int(instructions[discs.index(program)][1][1:-1])
            for leaf in leaves_dict[program]:
                total += leaf_price(leaf)
            calculated[program] = total
            return total


def validate_weight(program):
    temp = [leaf_price(x) for x in leaves_dict[program]]
    temp2 = sorted(temp)
    if temp == [temp[0]] * len(temp):
        return program
    else:
        if temp2[0]<temp2[1]:
            return validate_weight(leaves_dict[program][temp.index(temp2[0])])
        else:
            return validate_weight(leaves_dict[program][temp.index(temp2[-1])])



instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))]
leaves = []
leaves_dict = {}
calculated = {}
for i in instructions:
    for x in i:
        if ',' in x:
            i[i.index(x)] = x[:-1]
    if '->' in i:
        leaves += i[3:]
        leaves_dict[i[0]] = i[3:]
discs = [x[0] for x in instructions]
print([x for x in discs if x not in leaves])
print(validate_weight('eugwuhl'))
