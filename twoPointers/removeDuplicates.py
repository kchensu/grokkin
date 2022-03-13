def removeDuplicates(a):
    nextNonDuplicate = 0

    for i in range(1, len(a)):
        if a[nextNonDuplicate] != a[i]:
            a[nextNonDuplicate + 1] = a[i]
            nextNonDuplicate += 1
    return nextNonDuplicate + 1


a = [2, 3, 3, 3, 6, 9, 9]
b = [2, 2, 2, 11]
print(removeDuplicates(a))
print(removeDuplicates(b))
