import string


def permutationInAString(s1, s2):

    # check if the pattern is greater than the string, if greater then return false
    if len(s1) > len(s2):
        return False

    # create two hashmap to store the frequencies of each of the characters a-z
    s1Frequency, s2Frequency = dict.fromkeys(
        string.ascii_lowercase, 0), dict.fromkeys(string.ascii_lowercase, 0)

    # go through every char in s1 and add it to the s1 hashmap. Also we will init the s2 hashmpa with the first x characters in s1
    for i in range(len(s1)):
        s2Frequency[s2[i]] = 1 + s2Frequency.get(s2[i], 0)
        s1Frequency[s1[i]] = 1 + s1Frequency.get(s1[i], 0)

    # init match to 0
    matched = 0

    # if the chars in both hashmap matches, increase the match count
    for char in s1Frequency:
        if s1Frequency[char] == s2Frequency[char]:
            matched += 1

    # start the window size
    l = 0
    for r in range(len(s1), len(s2)):
        if matched == 26:
            return True

        s2Frequency[s2[r]] += 1
        if s1Frequency[s2[r]] == s2Frequency[s2[r]]:
            matched += 1
        elif s1Frequency[s2[r]] + 1 == s2Frequency[s2[r]]:
            matched -= 1

        s2Frequency[s2[l]] -= 1
        if s1Frequency[s2[l]] == s2Frequency[s2[l]]:
            matched += 1
        elif s1Frequency[s2[l]] - 1 == s2Frequency[s2[l]]:
            matched -= 1
        l += 1
    return matched == 26


s1 = "abc"
s2 = "cccccbabbbaaaa"
print(permutationInAString(s1, s2))
