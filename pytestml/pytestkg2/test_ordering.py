import pytest

@pytest.mark.run(order=2)
def test_foo1():
    assert True
@pytest.mark.run(order=1)
def test_bar2():
    assert True

def test_foo3():
    assert True

def test_bar4():
    assert True