def dutchNationalFlag(a):
    l = 0
    r = len(a)-1
    idx = 0
    while idx <= r:
        if a[idx] == 0:
            a[idx], a[l] = a[l], a[idx]
            idx += 1
            l += 1
        elif a[idx] == 1:
            idx += 1
        else:
            a[idx], a[r] = a[r], a[idx]
            r -= 1
    return a


a = [0, 1, 2, 0, 2, 1, 1]
# a = [2, 0, 1]
print(dutchNationalFlag(a))
