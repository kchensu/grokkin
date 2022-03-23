def squareArray(a):
    res = [0]*len(a)
    idx = len(res) - 1

    l, r = 0, len(a) - 1
    while l < r:
        leftSquared = a[l]*a[l]
        rightSquared = a[r]*a[r]
        if leftSquared > rightSquared:
            res[idx] = leftSquared
            l += 1
        else:
            res[idx] = rightSquared
            r -= 1
        idx -= 1
    return res


a = [-2, -1, 0, 2, 3]
b = [-3, -1, 0, 1, 2]
print(squareArray(a))
print(squareArray(b))
