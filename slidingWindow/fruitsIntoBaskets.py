def fruitsIntoBaskets(a):
    frequency = {}
    l = 0
    maxLength = 0

    for r in range(len(a)):
        if a[r] not in frequency:
            frequency[a[r]] = 0
        frequency[a[r]] += 1
        while len(frequency) > 2:
            frequency[a[l]] -= 1
            if frequency[a[l]] == 0:
                frequency.pop(a[l])
            l += 1
        maxLength = max(maxLength, r - l + 1)
    return maxLength


a = ['A', 'B', 'C', 'A', 'C']
print(fruitsIntoBaskets(a))
