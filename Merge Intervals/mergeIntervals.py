def mergeIntervals(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])

    mergedIntervals = [intervals[0]]
    for start, end in intervals[1:]:
        endValue = mergedIntervals[-1][1]
        if start <= endValue:
            mergedIntervals[-1][1] = max(endValue, end)
        else:
            mergedIntervals.append([start, end])
    return mergedIntervals

# def mergeIntervals(intervals):
#     intervals.sort(key=lambda x: x[0])
#     res = []
#     start = intervals[0][0]
#     end = intervals[0][1]
#     for i in range(1, len(intervals)):
#         interval = intervals[i]
#         if interval[0] <= end:
#             end = max(end, interval[1])
#         else:
#             res.append([start, end])
#             start = interval[0]
#             end = interval[1]
#     res.append([start, end])
#     return res


intervals = [[1, 4], [2, 5], [7, 9]]
print(mergeIntervals(intervals))
intervals = [[6, 7], [2, 4], [5, 9]]
print(mergeIntervals(intervals))
intervals = [[1, 4], [2, 6], [3, 5]]
print(mergeIntervals(intervals))
