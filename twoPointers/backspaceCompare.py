def backspaceCompare(s1, s2):
    s1Idx = len(s1) - 1
    s2Idx = len(s2) - 1
    while s1Idx >= 0 or s2Idx >= 0:
        i1 = getValidChar(s1, s1Idx)
        i2 = getValidChar(s2, s2Idx)

        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if s1[i1] != s2[i2]:
            return False
        s1Idx = i1 - 1
        s2Idx = i2 - 1
    return True


def getValidChar(s, index):
    backspaceCount = 0
    while index > 0:
        if s[index] == '#':
            backspaceCount += 1
        elif backspaceCount > 0:
            backspaceCount -= 1
        else:
            break
        index -= 1
    return index


str1 = "xp#"
str2 = "xyz##"
print(backspaceCompare(str1, str2))
