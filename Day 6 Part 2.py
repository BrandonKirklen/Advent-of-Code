#!/usr/bin/python2.4 -tt
from pprint import pprint


def createLightArray(size):
    return [[0 for x in range(size)] for x in range(size)]


def toggleLights(startIndex, stopIndex, array):
    for x in range(startIndex[0], stopIndex[0]+1):
        for y in range(startIndex[1], stopIndex[1]+1):
            array[x][y] += 2
    return array


def turnOffLights(startIndex, stopIndex, array):
    for x in range(startIndex[0], stopIndex[0]+1):
        for y in range(startIndex[1], stopIndex[1]+1):
            if array[x][y] > 0:
                array[x][y] -= 1
    return array


def turnOnLights(startIndex, stopIndex, array):
    for x in range(startIndex[0], stopIndex[0]+1):
        for y in range(startIndex[1], stopIndex[1]+1):
            array[x][y] += 1
    return array


def stringIndexToInt(cordString):
    cordList = cordString.split(",")
    return (int(cordList[0]), int(cordList[1]))


def lightProcessor(string, array):
    lightList = string.split(" ")
    if lightList[0] == "toggle":
        startIndex = stringIndexToInt(lightList[1])
        stopIndex = stringIndexToInt(lightList[3])
        toggleLights(startIndex, stopIndex, array)
    elif lightList[1] == "on":
        startIndex = stringIndexToInt(lightList[2])
        stopIndex = stringIndexToInt(lightList[4])
        turnOnLights(startIndex, stopIndex, array)
    elif lightList[1] == "off":
        startIndex = stringIndexToInt(lightList[2])
        stopIndex = stringIndexToInt(lightList[4])
        turnOffLights(startIndex, stopIndex, array)


def analytics(array):
    lightBrightness = 0
    for x in range(len(array)):
        for y in range(len(array[0])):
            lightBrightness += array[x][y]
    print("Light Brightness: " + str(lightBrightness))


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def ploter(array):
    import numpy as np
    import matplotlib as ml
    import matplotlib.pyplot as plt

    H = np.array(array)
    fig = plt.figure(figsize=(6, 3.2))

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(H)
    ax.set_aspect('equal')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    plt.show()


def tester():
    print("test")

    test(stringIndexToInt("533,331"), (533, 331))


def main():
    with open("lightList") as f:
        content = [line.rstrip('\n') for line in f]
    lightArray = createLightArray(1000)
    analytics(lightArray)
    # toggleLights((0, 0), (5, 5), lightArray)
    # turnOnLights((5, 5), (10, 10), lightArray)
    # turnOffLights((0, 0), (5, 5), lightArray)
    # pprint(lightArray)
    for string in content:
        lightProcessor(string, lightArray)
    analytics(lightArray)
    ploter(lightArray)


if __name__ == '__main__':
    main()
