#!/usr/bin/python2.4 -tt


def containsThreeVowels(string):
    vowelCount = [c for c in string if c in ["a", "e", "i", "o", "u"]]
    if len(vowelCount) >= 3:
        return True
    else:
        return False


def doubleLetter(string):
    priorLetter = ""
    for s in string:
        if s == priorLetter:
            return True
        else:
            priorLetter = s
    return False


def containsBadString(string):
    return ((string.find("ab") != -1) or
            (string.find("cd") != -1) or
            (string.find("pq") != -1) or
            (string.find("xy") != -1))


def letterPair(string):
    for i, s in enumerate(string):
        if string[i+2:].find(string[i:i+2]) >= 0:
            return True
    return False


def splitPair(string):
    for i, s in enumerate(string[:-2]):
        if s == string[i + 2]:
            return True
    else:
        return False


def niceString(string):
    return (containsThreeVowels(string) and
            doubleLetter(string) and
            containsBadString(string) == False)


def newNiceString(string):
    return (letterPair(string) and splitPair(string))


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def tester():
    print("Three Vowels Test:")
    test(containsThreeVowels("aeiouaeiouaeiou"), True)
    test(containsThreeVowels("aei"), True)
    test(containsThreeVowels("xazegov"), True)
    test(containsThreeVowels("ccbbeepp"), False)
    print

    print("Double Letter Test:")
    test(doubleLetter("aeiouaeiouaeiou"), False)
    test(doubleLetter("aeei"), True)
    test(doubleLetter("xazeggov"), True)
    test(doubleLetter("ccbbeepp"), True)
    print

    print("Bad String Test:")
    test(containsBadString("aeiouaeiouaeiou"), False)
    test(containsBadString("abeei"), True)
    test(containsBadString("tete"), False)
    test(containsBadString("ccdbeepp"), True)
    print

    print("Nice String Test:")
    test(niceString("ugknbfddgicrmopn"), True)
    test(niceString("jchzalrnumimnmhp"), False)
    test(niceString("haegwjzuvuyypxyu"), False)
    test(niceString("dvszwmarrgswjxmb"), False)
    print

    print("Split Pair:")
    test(splitPair("ugknbfdgdicrmopn"), True)
    test(splitPair("jchzalrnumimnmhp"), True)
    test(splitPair("abcdefg"), False)
    test(splitPair("aaa"), True)
    print

    print("Letter Pair:")
    test(letterPair("xyxy"), True)
    test(letterPair("aabcdefgaa"), True)
    test(letterPair("aaa"), False)
    test(letterPair("asdfoiweursdf"), True)
    print

def main():
    tester()
    with open("naughtyList") as f:
        content = [line.rstrip('\n') for line in f]
    totalNice = 0
    newNice = 0
    for string in content:
        if niceString(string):
            totalNice += 1
        if newNiceString(string):
            newNice += 1
    print(totalNice)
    print newNice


if __name__ == '__main__':
    main()
