import re


def getMulNumbersList(tempStr):
    return re.findall(r"mul\((\d+),(\d+)\)", tempStr)


def splitDo(tempStr):
    return re.split(r"do\(\)", tempStr)


def splitDont(tempStr):
    return re.split(r"don't\(\)", tempStr)


sum = 0
with open("input.txt") as testInput:
    textInfor = testInput.read()
    textInfor.replace("\n", "")
    dontSplit = splitDont(textInfor)
    procFirst = getMulNumbersList(dontSplit[0])
    for i, j in procFirst:
        sum += int(i) * int(j)
    for strSplit in dontSplit[1:]:
        doSplit = splitDo(strSplit)
        if len(doSplit) is not None:
            for finSplit in doSplit[1:]:
                listMul = getMulNumbersList(finSplit)
                for i, j in listMul:
                    sum += int(i) * int(j)
    print(sum)
