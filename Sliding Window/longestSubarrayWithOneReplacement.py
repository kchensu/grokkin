def longestSubarrywithOneReplacement(a, k):
    l = 0
    maxLength = 0
    maxOneCount = 0

    for r in range(len(a)):
        if a[r] == 1:
            maxOneCount += 1

        while (r - l + 1 - maxOneCount) > k:
            if a[l] == 1:
                maxOneCount -= 1
            l += 1
        maxLength = max(maxLength, r - l + 1)
    return maxLength


a = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
print(longestSubarrywithOneReplacement(a, 2))
