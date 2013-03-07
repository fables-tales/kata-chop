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

##Day 2

(today coming to you from Google campus)

I started by looking if any refactorings could be made to my existing solution.
The main thing that I felt could be done was to make it so that the tests were
not specific to the chop1 function but could instead be parameterised to take a
function, and run all the tests against that. I extracted the run\_chop
function which takes a chopper like function to test.

For todays implementation I decided that a simple recursive binary search would
be a good next implementation. This is the "other" implementation that is
commonly taught in algorithms classes, and is an implementation that I'm
familiar with.

Again I started with a simple implementation that returns -1 and hooked up
the tests to the chopper (this time called chop2) to ensure that everything was
ready to be hacked upon.

The output from nose clearly showed the first implementation still passes,
but the second one fails, as expected:

```
:!nosetests
.F
======================================================================
FAIL: chopper_tests.test_chop2
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/nose-1.2.1-py2.7.egg/nose/case.py", line 197, i
n runTest
    self.test(*self.arg)
  File "/Users/sam/dev/kata-chop/tests/chopper_tests.py", line 30, in test_chop2
    run_chop(chopper.chop2)
  File "/Users/sam/dev/kata-chop/tests/chopper_tests.py", line 6, in run_chop
    assert 0 == chop_function(1, [1])
AssertionError

----------------------------------------------------------------------
```

###First Implementation

```python
def chop2(item, values, min = 0, max = None):
    if max is None:
        max = len(values)-1

    mid = (max+min)/2

    if min > max:
        return -1
    elif values[mid] > item:
        return chop2(item, values, min, mid-1)
    elif values[mid] < item:
        return chop2(item, values, mid+1, max)
    else:
        return values[mid]
```

Problem: returns values[mid] rather than mid.

###Second Implementation

```python
def chop2(item, values, min = 0, max = None):
    if max is None:
        max = len(values)-1

    mid = (max+min)/2

    if min > max:
        return -1
    elif values[mid] > item:
        return chop2(item, values, min, mid-1)
    elif values[mid] < item:
        return chop2(item, values, mid+1, max)
    else:
        return mid
```

This seems to pass all the tests. As a matter of course I noted that the
calculation to compute the midpoint of the high and low values is now
duplicated, so I pulled it out into it's own method and ran the tests again.

It's worth noting that whilst we had roughly the same number of errors today as
yesterday, it took me a lot less time to actually come up with something that I
thought I could run that would be roughly correct. This is partly due to having
thought about today's solution in 'down' time yesterday, and having yesterday's
solution open on my computer whilst implementing this solution.
