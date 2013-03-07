import chopper

def run_chop(chop_function):
    assert -1 == chop_function(3, [])
    assert -1 == chop_function(3, [1])
    assert 0 == chop_function(1, [1])
    #
    assert 0 == chop_function(1, [1, 3, 5])
    assert 1 == chop_function(3, [1, 3, 5])
    assert 2 == chop_function(5, [1, 3, 5])
    assert -1 == chop_function(0, [1, 3, 5])
    assert -1 == chop_function(0, [1, 3, 5])
    assert -1 == chop_function(0, [1, 3, 5])
    assert -1 == chop_function(0, [1, 3, 5])
    #
    assert 0 == chop_function(1, [1, 3, 5, 7])
    assert 1 == chop_function(3, [1, 3, 5, 7])
    assert 2 == chop_function(5, [1, 3, 5, 7])
    assert 3 == chop_function(7, [1, 3, 5, 7])
    assert -1 == chop_function(0, [1, 3, 5, 7])
    assert -1 == chop_function(2, [1, 3, 5, 7])
    assert -1 == chop_function(4, [1, 3, 5, 7])
    assert -1 == chop_function(6, [1, 3, 5, 7])
    assert -1 == chop_function(8, [1, 3, 5, 7])

def test_chop1():
    run_chop(chopper.chop1)
