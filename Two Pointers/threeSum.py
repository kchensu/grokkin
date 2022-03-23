
# x + y + z = 0
# y + z = -x


def threeSum(a):
    a.sort()
    res = []
    for i in range(len(a)):
        if i > 0 and a[i] == a[i-1]:
            continue
        l = i + 1
        r = len(a) - 1
        while l < r:
            currSum = a[l] + a[r]
            if currSum == -1*a[i]:
                res.append([a[i], a[l], a[r]])
                l += 1
                r -= 1
                while l < r and a[l] == a[l-1]:
                    l += 1
                while l < r and a[r] == a[r+1]:
                    r -= 1
            elif -1*a[i] > currSum:
                l += 1
            else:
                r -= 1
    return res


a = [-1, 0, 1, 2, -1, -4]
b = [-3, 0, 1, 2, -1, 1, -2]
c = [-5, 2, -1, -2, 3]
print(threeSum(a))
print(threeSum(b))
print(threeSum(c))
