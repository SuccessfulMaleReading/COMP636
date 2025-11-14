n = int(input())
arr = list(map(int, input().split()))

maxScore = max(arr)

while maxScore in arr:
    arr.remove(maxScore)

runnerUp = max(arr)

print(runnerUp)