def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        previous_interval = merged[-1]

        if current_interval[0] <= previous_interval[1]:

            merged[-1] = [previous_interval[0], max(previous_interval[1], current_interval[1])]
        else:
            merged.append(current_interval)

    return merged

intervals = [[4, 8], [7, 9], [10, 15], [1, 3]]
print(intervals)
result = merge_intervals(intervals)
print(result)
