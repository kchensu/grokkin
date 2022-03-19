

def topKFrequent(nums, k):
    count = {}
    freq = []
    for i in range(len(nums) + 1):
        freq.append([])
    for i in range(len(nums)):
        count[nums[i]] = 1 + count.get(nums[i], 0)

    for key, val in count.items():
        freq[key].append(val)
    res = []
    for i in reversed(range(len(freq) - 1)):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
