def happyNumber(n):
    slow = n
    fast = n
    while True:
        slow = findSquared(slow)
        fast = findSquared(findSquared(fast))
        if fast == slow:
            break
    return slow == 1


def findSquared(n):
    currSum = 0
    while n > 0:
        digit = n % 10
        digit = digit**2
        currSum += digit
        n = n//10
    return currSum


print(happyNumber(12))
print(happyNumber(23))
