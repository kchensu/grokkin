from collections import deque


# def subarrayProduct(a, t):
#     res = []
#     product = 1
#     l = 0
#     for r in range(len(a)):
#         product = product * a[r]
#         while product >= t and l < r:
#             product = product / a[l]
#             l += 1
#         temp = deque()
#         for i in range(r, l-1, -1):
#             temp.appendleft(a[i])
#             res.append(list(temp))
#     return len(res)

def subarrayProduct(a, t):
    count = 0
    l = 0
    product = 1
    for r in range(len(a)):
        product = product * a[r]
        while product >= t and l <= r:
            product = product / a[l]
            l += 1
        count += r - l + 1
    return count


a = [10, 5, 2, 6]
t = 100
print(subarrayProduct(a, t))
