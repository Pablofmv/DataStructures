def PointsCoverSorted(array):
    n = len(array)
    left = 0
    segments = []

    while left < n:
        l, r = array[left], array[left] + 2
        left += 1
        segments.append([l,r])
        while left < n and array[left] <= r:
            left += 1
    
    print(segments)
    return segments

PointsCoverSorted([0,2,3,4])

