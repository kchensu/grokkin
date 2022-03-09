def averageSubarrayOfsizeK(a, k):
    res = []
    total = 0
    l = 0
    for r in range(len(a)):
        total += a[r]
        if r >= k - 1:
            res.append(total/k)
            total = total - a[l]
            l += 1
    return res


a = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(averageSubarrayOfsizeK(a, 5))
