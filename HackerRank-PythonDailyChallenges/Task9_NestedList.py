nestList = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nestList.append([name, score])

lowestNum = min(nestList)
for lowestNum in nestList:
    nestList.remove(lowestNum)

Scores = [score for name, score in nestList]
secondLowest = sorted(set(Scores))[1]
second_lowest_students = [name for name, score in Scores if score == secondLowest]

for name in sorted(second_lowest_students):
    print(name)
