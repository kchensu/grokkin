def longestSubstringWithSameLettersReplacement(s, k):
    maxLength = 0
    l = 0
    chars = {}
    for r in range(len(s)):
        if s[r] not in chars:
            chars[s[r]] = 0
        chars[s[r]] += 1
        while (r - l + 1) - max(chars.values()) > k:
            chars[s[l]] -= 1
            l += 1
        maxLength = max(maxLength, r - l + 1)
    return maxLength


s1 = "aabccbb"
k1 = 2
s2 = "abbcb"
k2 = 1
s3 = "abccde"
k3 = 1
print(longestSubstringWithSameLettersReplacement(s1, k1))
print(longestSubstringWithSameLettersReplacement(s2, k2))
print(longestSubstringWithSameLettersReplacement(s3, k3))
