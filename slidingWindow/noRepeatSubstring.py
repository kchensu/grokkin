def noRepeatSubstring(s):
    frequency = {}
    l = 0
    maxLength = 0

    for r, char in enumerate(s):
        if char in frequency:
            l = max(l, frequency[char] + 1)
        frequency[char] = r
        maxLength = max(maxLength, r - l + 1)
    return maxLength


s = "abccde"
print(noRepeatSubstring(s))
