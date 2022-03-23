from heapq import *


def findKSmallestNumber(nums, k):
    minHeap = []

    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return minHeap[0]


def main():
    print(f"Kth smallest number is: {findKSmallestNumber([1,5,12,2,11,5], 3)}")
    # print(f"Kth smallest number is: {findKSmallestNumber([1,5,12,2,11,5], 4)}")
    # print(f"Kth smallest number is: {findKSmallestNumber([5,12,11,-1,12], 3)}")


main()
