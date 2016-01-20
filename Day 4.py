#!/usr/bin/python2.4 -tt


def md5hash(string):
    import hashlib
    magic = hashlib.md5()
    magic.update(string)
    return magic.hexdigest()


def main():
    secret = "bgvyzdsv"
    answer = 0
    test = 0
    while answer == 0:
        testHash = md5hash(secret + str(test))[0:6]
        if testHash == "000000":
            answer = test
        else:
            test += 1
    print(answer)


if __name__ == '__main__':
    main()
