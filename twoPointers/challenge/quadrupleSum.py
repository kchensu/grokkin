def quadrupleSum(a, target):
    a.sort()
    quadruplets = []
    for i in range(len(a)):
        if i > 0 and a[i] == a[i-1]:
            continue
        for j in range(i + 1, len(a)-3):
            if j > i + 1 and a[j] == a[j-1]:
                continue
            l = j + 1
            r = len(a) - 1
            while l < r:
                currSum = a[i] + a[j] + a[l] + a[r]
                if currSum == target:
                    quadruplets.append([a[i], a[j], a[l], a[r]])
                    l += 1
                    r -= 1
                    while l < r and a[l] == a[l-1]:
                        l += 1
                    while l < r and a[r] == a[r+1]:
                        r -= 1
                elif currSum > target:
                    r -= 1
                else:
                    l += 1
    return quadruplets


a = [1, 0, -1, 0, -2, 2]
target = 0
print(quadrupleSum(a, target))
