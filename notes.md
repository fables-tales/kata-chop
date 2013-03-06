#Chop Kata

##Day 1

Setup nose tests and chopper that returns -1 on all calls. First assertion
error hit as expected:

```
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/nose-1.2.1-py2.7.egg/nose/case.py", line 197, in runTest
    self.test(*self.arg)
  File "/Users/sam/dev/kata-chop/tests/chopper_tests.py", line 6, in test_chop_1_
    assert 0 == chopper.chop_1(1, [1])
AssertionError
```

Chosen implementation: iterative binary chop using a while loop. See the chop1
function.

###First implementation:

```python
def chop1(item, values):
    high = len(values)-1
    low  = 0

    while high >= low:
        mid = (high + low)/2
        if values[mid] < item:
            low = mid
        elif values[mid] > item:
            high = mid
        else:
            return mid
    return -1
```

The implementation here goes into an infinite loop. This is because we need to
update high or low to not be the mid item, but the mid item +1 or -1
respectively (this reduces the size of the range when the array is of length 1)

###Second implementation

```python
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
```

This passes all the tests given by the kata, the infinite loop is solved by
moving the new bounds in the direction of where the expected value is.
