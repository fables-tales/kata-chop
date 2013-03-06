import chopper

def test_chop1():
    assert -1 == chopper.chop1(3, [])
    assert -1 == chopper.chop1(3, [1])
    assert 0 == chopper.chop1(1, [1])
    #
    assert 0 == chopper.chop1(1, [1, 3, 5])
    assert 1 == chopper.chop1(3, [1, 3, 5])
    assert 2 == chopper.chop1(5, [1, 3, 5])
    assert -1 == chopper.chop1(0, [1, 3, 5])
    assert -1 == chopper.chop1(0, [1, 3, 5])
    assert -1 == chopper.chop1(0, [1, 3, 5])
    assert -1 == chopper.chop1(0, [1, 3, 5])
    #
    assert 0 == chopper.chop1(1, [1, 3, 5, 7])
    assert 1 == chopper.chop1(3, [1, 3, 5, 7])
    assert 2 == chopper.chop1(5, [1, 3, 5, 7])
    assert 3 == chopper.chop1(7, [1, 3, 5, 7])
    assert -1 == chopper.chop1(0, [1, 3, 5, 7])
    assert -1 == chopper.chop1(2, [1, 3, 5, 7])
    assert -1 == chopper.chop1(4, [1, 3, 5, 7])
    assert -1 == chopper.chop1(6, [1, 3, 5, 7])
    assert -1 == chopper.chop1(8, [1, 3, 5, 7])
