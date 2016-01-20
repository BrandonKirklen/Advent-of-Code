#!/usr/bin/python2.4 -tt


def squareFootage(string):
    return [int(s) for s in string.split("x") if s.isdigit()]


def paperSize(tuple):
    side1 = 2*tuple[0]*tuple[1]
    side2 = 2*tuple[1]*tuple[2]
    side3 = 2*tuple[2]*tuple[0]
    return side1 + side2 + side3 + min(side1, side2, side3)/2


def ribbonSize(tuple):
    tuple.sort()
    return 2*tuple[0] + 2*tuple[1] + tuple[0]*tuple[1]*tuple[2]


def wrappingPaper(listOfPackages):
    measurements = [squareFootage(string) for string in listOfPackages]
    totalSquareFeet = 0
    for packageSizes in measurements:
        totalSquareFeet += paperSize(packageSizes)
    return totalSquareFeet


def ribbon(listOfPackages):
    measurements = [squareFootage(string) for string in listOfPackages]
    totalRibbon = 0
    for ribbonSizes in measurements:
        totalRibbon += ribbonSize(ribbonSizes)
    return totalRibbon


def main():
    with open("packageList") as f:
        content = [line.rstrip('\n') for line in f]
    print("wrapping paper:  " + str(wrappingPaper(content)) + " (ft^2)")
    print("ribbon:          " + str(ribbon(content)) + " (ft)")

if __name__ == '__main__':
    main()
