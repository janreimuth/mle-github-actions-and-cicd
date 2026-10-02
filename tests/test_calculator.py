from src.calculator import add, substract


def test_add():
    assert add(1, 2) == 3
    assert add(-2, 2) == 0
    assert add(0, 0) == 0

def test_substract():
    assert substract(5, 2) == 3
    assert substract(2, 2) == -4
    assert substract(2, 2) == 0
    assert substract(0, 0) == 0