#!/usr/bin/python2.4 -tt


def followInstructions(instructions):

    x, y = (0, 0)
    yield x, y

    for instruction in instructions:
        if instruction == ">":
            x += 1
        elif instruction == "<":
            x -= 1
        elif instruction == "^":
            y += 1
        elif instruction == "v":
            y -= 1

        yield (x, y)


def listHouses(instructions):
    from collections import defaultdict

    visitedHouses = defaultdict(int)
    for location in followInstructions(instructions):
        visitedHouses[location] += 1
    return visitedHouses.keys()


def listHousesRobot(instructions):
    from collections import defaultdict

    visitedHouses = defaultdict(int)
    print instructions
    realSantaInstructions = [instruction for i,
                             instruction in enumerate(instructions) if
                             i % 2 == 0]
    robotSantaInstructions = [instruction for i,
                              instruction in enumerate(instructions) if
                              i % 2 == 1]
    print realSantaInstructions
    print robotSantaInstructions
    for location in followInstructions(realSantaInstructions):
        visitedHouses[location] += 1
    for location in followInstructions(robotSantaInstructions):
        visitedHouses[location] += 1
    return visitedHouses.keys()


def main():
    with open("flightInstructions", "r") as f:
        instructions = f.read()
        houses1 = listHouses(instructions)
        houses2 = listHousesRobot(instructions)

    print len(houses1)
    print len(houses2)


if __name__ == '__main__':
    main()
