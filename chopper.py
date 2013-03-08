
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

def list_midpoint(values):
    return midpoint(0,len(values))

def left_subtree(values):
    return values[:list_midpoint(values)]

def right_subtree(values):
    return values[list_midpoint(values)+1:]

def chop3(item, values):
    if len(values) == 0:
        return -1

    mid = list_midpoint(values)

    if values[mid] > item:
        return chop3(item, left_subtree(values))
    elif values[mid] < item:
        chop_result = chop3(item, right_subtree(values))
        return mid + 1 + chop_result if chop_result != -1 else -1
    else:
        return mid
