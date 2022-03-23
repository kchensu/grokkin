from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):

        return (self.x ** 2+self.y ** 2) > (other.x ** 2+other.y ** 2)


def findClosestPoints(points, k):
    minHeap = []
    for i in range(k):
        heappush(minHeap, points[i])

    for i in range(k, len(points)):
        if points[i].x**2 + points[i].y**2 < minHeap[0].x**2 + minHeap[0].y**2:
            heappop(minHeap)
            heappush(minHeap, points[i])

    return minHeap


def main():
    res = findClosestPoints([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    for point in res:
        print([point.x, point.y])


main()
