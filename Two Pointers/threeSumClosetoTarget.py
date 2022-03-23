def threeSumCloseToTarget(a, t):
    a.sort()
    res = sum(a[:3])
    for i in range(len(a) - 2):
        l = i + 1
        r = len(a) - 1
        while l < r:
            currSum = a[i] + a[l] + a[r]
            if currSum == t:
                return currSum
            if abs(currSum - t) < abs(res - t):
                res = currSum

            if currSum > t:
                r -= 1
            else:
                l += 1
    return res


a = [-1, 2, 1, -4]
t = 1
print(threeSumCloseToTarget(a, t))
