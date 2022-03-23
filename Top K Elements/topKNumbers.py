from heapq import *


def findKLargestElem(nums, k):
    result = []

    for i in range(k):
        heappush(result, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > result[0]:
            heappop(result)
            heappush(result, nums[i])
    return result


def main():
    print(f"Top K elements {findKLargestElem([3,1,5,12,2,11], 3)}")
    print(f"Top K elements {findKLargestElem([5,12,11,-1.12], 3)}")


main()
