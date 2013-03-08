
def midpoint(a, b):
    return (a+b)/2

def chop1(item, values):
    high = len(values)-1
    low  = 0

    while high >= low:
        mid = midpoint(high, low)
        if values[mid] < item:
            low = mid + 1
        elif values[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1

def chop2(item, values, min = 0, max = None):
    if max is None:
        max = len(values)-1

    mid = midpoint(max, min)

    if min > max:
        return -1
    elif values[mid] > item:
        return chop2(item, values, min, mid-1)
    elif values[mid] < item:
        return chop2(item, values, mid+1, max)
    else:
        return mid
