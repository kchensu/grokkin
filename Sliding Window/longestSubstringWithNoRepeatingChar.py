def longestSubstringWithNoReeaptingChar(s):
    maxLegth = 0
    l = 0
    chars = set()
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        maxLegth = max(maxLegth, r - l + 1)
    return maxLegth


s = "aabccbb"
print(longestSubstringWithNoReeaptingChar(s))
