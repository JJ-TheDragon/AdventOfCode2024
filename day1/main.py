
col1 = []
col2 = []
with open("input.txt", "r") as f:
    for lines in f:
        col1.append(int(lines.split()[0]))
        col2.append(int(lines.split()[1]))
displacement = 0
col1.sort()
col2.sort()
for i in range(len(col1)):
    displacement += abs(col1[i] - col2[i])
print(displacement)
similarity = 0
simDict = {}
for i in col2:
    if i in simDict:
        simDict[i] += 1
    else:
        simDict[i] = 1
for i in col1:
    if i in simDict:
        similarity += i * simDict[i]

print(similarity)
