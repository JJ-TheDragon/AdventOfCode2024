import re
sum = 0
with open("input.txt") as testInput:
    for lines in testInput:
        regOutput = re.findall(r"mul\((\d+),(\d+)\)", lines)
        for i, j in regOutput:
            sum += int(i) * int(j)
print(sum)
