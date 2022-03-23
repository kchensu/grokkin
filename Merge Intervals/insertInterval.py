def insertInterval(intervals, interval):
    res = []
    newIntervalStart = interval[0]
    newIntervalEnd = interval[1]
    for i in range(len(intervals)):
        if newIntervalEnd < intervals[i][0]:
            res.append(interval)
            return res + intervals[i:]
        elif newIntervalStart > intervals[i][1]:
            res.append(intervals[i])
        else:
            interval = [min(newIntervalStart, intervals[i][0]),
                        max(newIntervalEnd, intervals[i][1])]
    res.append(interval)

    return res


intervals = [[1, 3], [5, 7], [11, 12]]
interval = [8, 9]
print(insertInterval(intervals, interval))
