# def threeSumSmallest(a, t):
#     a.sort()
#     res = []
#     for i in range(len(a)):
#         l = i + 1
#         r = len(a) - 1
#         while l < r:
#             currSum = a[i] + a[l] + a[r]
#             if currSum < t:
#                 for j in reversed(range(l, r)):
#                     res.append([a[i], a[l], a[r]])
#                 l += 1
#             else:
#                 r -= 1

#     return res

def threeSumSmallest(a, t):
    a.sort()
    count = 0
    for i in range(len(a)):
        l = i + 1
        r = len(a) - 1
        while l < r:
            curSum = a[i] + a[l] + a[r]
            if curSum < t:
                count += r - l
                l += 1
            else:
                r -= 1
    return count


a = [-1, 0, 2, 3]
b = [-1, 4, 2, 1, 3]
t = 5
# print(threeSumSmallest(a, t))
print(threeSumSmallest(b, t))
