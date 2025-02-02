def PointsCoverSorted(array):
    segments = []
    left = 0
    n = len(array)
    while left < n:
        l,r = array[left],array[left]+2
        segments.append([l,r])
        left = left + 1
        while left < n and array[left] <= r:
            left = left + 1
    print(segments)  
    return segments


PointsCoverSorted([0,4,8])

