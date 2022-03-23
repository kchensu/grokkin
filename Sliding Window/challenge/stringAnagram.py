def stringAnagram(s1, s2):
    if len(s1) > len(s2):
        return []

    s1Frequency, s2Frequency = {}, {}

    for i in range(len(s1)):
        s1Frequency[s1[i]] = 1 + s1Frequency.get(s1[i], 0)
        s2Frequency[s2[i]] = 1 + s2Frequency.get(s2[i], 0)

    if s1Frequency == s2Frequency:
        res = [0]
    else:
        res = []

    l = 0
    for r in range(len(s1), len(s2)):
        s2Frequency[s2[r]] = 1 + s2Frequency.get(s2[r], 0)
        s2Frequency[s2[l]] -= 1
        if s2Frequency[s2[l]] == 0:
            s2Frequency.pop(s2[l])
        l += 1
        if s1Frequency == s2Frequency:
            res.append(l)
    return res


s1 = "abc"
s2 = "abbcabc"
print(stringAnagram(s1, s2))
