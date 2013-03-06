def chop1(item, values):
    high = len(values)-1
    low  = 0

    while high >= low:
        mid = (high + low)/2
        if values[mid] < item:
            low = mid + 1
        elif values[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1
