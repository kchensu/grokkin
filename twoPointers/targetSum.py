def targetSum(a, t):
    l = 0
    r = len(a) - 1

    while l < r:
        currSum = a[l] + a[r]
        if currSum == t:
            return [l, r]
        if currSum > t:
            r -= 1
        elif currSum < t:
            l += 1
    return [-1, -1]


a = [2, 5, 9, 11]
t = 11
print(targetSum(a, t))
