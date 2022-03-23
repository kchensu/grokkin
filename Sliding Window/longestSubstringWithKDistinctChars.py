def longestSubstringWithKDistinctChars(s, k):
    h = {}
    l = 0
    maxLength = 0
    for r, c in enumerate(s):
        if c not in h:
            h[c] = 0
        h[c] += 1
        while len(h) > k:
            h[s[l]] -= 1
            if h[s[l]] == 0:
                h.pop(s[l])
            l += 1
        maxLength = max(maxLength, r - l + 1)
    return maxLength


s = "araaci"
k = 2
print(longestSubstringWithKDistinctChars(s, k))
