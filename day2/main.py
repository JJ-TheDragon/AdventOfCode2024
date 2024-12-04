import copy


def checkAscending(checkList):
    testList = copy.copy(checkList)
    testList.sort()
    return testList == checkList


def checkDescending(checkList):
    testList = copy.copy(checkList)
    testList.sort(reverse=True)
    return testList == checkList


def checkDelta(checkList):
    for i in range(len(checkList)-1):
        delta = abs(checkList[i] - checkList[i+1])
        if delta > 3 or delta < 1:
            return False
    return True


safeTest = 0
with open("input.txt", "r") as f:
    for lines in f:
        test = lines.split()
        test = [int(t) for t in test]
        if (checkDelta(test)) and (checkAscending(test) or checkDescending(test)):
            safeTest += 1
        else:
            for i in range(len(test)):
                testCopy = copy.copy(test)
                testCopy.pop(i)
                if (checkDelta(testCopy)) and (checkAscending(testCopy) or checkDescending(testCopy)):
                    safeTest += 1
                    break
print(safeTest)
