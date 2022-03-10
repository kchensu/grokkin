def maximumSubarrayOfSizeK(a, k):
    maxSum = 0
    windowSum = 0
    l = 0
    for r in range(len(a)):
        windowSum = windowSum + a[r]
        if r >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum = windowSum - a[l]
            l += 1
    return maxSum


def maxSub(a, k):

    maxSum = sum(a[:k])
    l = 0
    currSum = maxSum
    for r in range(k, len(a)):
        currSum = currSum + a[r] - a[l]
        maxSum = max(currSum, maxSum)
        l += 1
    return maxSum


a = [2, 1, 5, 1, 3, 2]
k = 3
# print(maximumSubarrayOfSizeK(a, k))
print(maxSub(a, k))
