def smallestSubarrayGivenK(a, k):
    l = 0
    currSum = 0
    minLength = float('inf')
    for r in range(len(a)):
        currSum = currSum + a[r]
        while currSum >= k:
            minLength = min(minLength, r - l + 1)
            currSum = currSum - a[l]
            l += 1
    if minLength == float('inf'):
        return 0
    return minLength


a = [3, 4, 1, 1, 6]
k = 8
print(smallestSubarrayGivenK(a, k))
