def longestSubstringWithSameLettersReplacement(s, k):
    maxLength = 0
    l = 0
    chars = {}
    maxLetterCount = 0
    for r in range(len(s)):
        if s[r] not in chars:
            chars[s[r]] = 0
        chars[s[r]] += 1
    maxLetterCount = max(maxLetterCount, chars[s[r]])


s = "aabccbb"
k = 2
print(longestSubstringWithSameLettersReplacement(s, k))
