from time import sleep
import pytest


def test_rurun1():
    sleep(0.5)
    assert 1 == 2

def test_rerun2():
    sleep(0.5)
    assert 2 == 2
@pytest.mark.flaky(reruns=5)
def test_rurun3():
    sleep(0.5)
    assert 3 == 2