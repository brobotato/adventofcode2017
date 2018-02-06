import math, os

instructions = [l.split() for l in open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3]))]
instructions = int(instructions[0][0])
stresscalculated = {}


def position(number, side="lul"):
    x = 1
    y = 1
    if side == "lul":
        side = math.ceil(math.sqrt(number))
    if number == 1:
        return oneloc(number, side)
    if side % 2 == 0:
        if number <= side ** 2 - 4 * (side - 1):
            return [position(number, side - 1)[0], position(number, side - 1)[1] + 1]
        if number < side ** 2 - 3 * (side - 1):
            y = side
            y -= side ** 2 - 3 * (side - 1) - number
        elif number < side ** 2 - 2 * (side - 1):
            y = side
            x = side
            x -= side ** 2 - 2 * (side - 1) - number
        elif number < side ** 2 - side + 1:
            x += side - 1
            y += side ** 2 - side + 1 - number
        else:
            x += side ** 2 - number
    else:
        x = side
        y = side
        if number <= side ** 2 - 4 * (side - 1):
            return [position(number, side - 1)[0] + 1, position(number, side - 1)[1]]
        if number < side ** 2 - 3 * (side - 1):
            y = 1
            y += side ** 2 - 3 * (side - 1) - number
        elif number < side ** 2 - 2 * (side - 1):
            x = 1
            y = 1
            x += side ** 2 - 2 * (side - 1) - number
        elif number < side ** 2 - side + 1:
            x -= side - 1
            y -= side ** 2 - side + 1 - number
        else:
            x -= side ** 2 - number
    return [x, y]


def oneloc(number, side="lul"):
    if side == "lul":
        side = math.ceil(math.sqrt(number))
    if side % 2 == 0:
        location = [side / 2, side / 2 + 1]
    else:
        location = [math.ceil(side / 2), math.ceil(side / 2)]
    return location


def distance(number):
    location = oneloc(number)
    coords = position(number)
    return [coords[0] - location[0], coords[1] - location[1]]


def nearby(number):
    nearbylist = []
    side = math.ceil(math.sqrt(number))
    for x in range(number - 1, 0, -1):
        if position(number, side)[0] - position(x, side)[0] in [-1, 0, 1] and position(number, side)[1] - \
                position(x, side)[1] in [-1, 0, 1]:
            nearbylist.append(x)
    return nearbylist


def stress(number):
    stressval = 0
    if number == 1:
        return 1
    else:
        for x in (nearby(number)):
            if x in stresscalculated:
                stressval += stresscalculated[x]
            else:
                stressval += stress(x)
                stresscalculated[x] = stress(x)
    stresscalculated[number] = stressval
    return stressval


print(distance(instructions))
lol = True
ha = 1
while (lol):
    if stress(ha) > instructions:
        lol = False
    else:
        ha += 1
print(stress(ha))
