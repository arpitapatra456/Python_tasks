import pytest
import sys

@pytest.mark.skip()
def test_payment():
    assert 100 + 50 == 150
def test_add():
    assert 2 + 3 == 5
def test_sub():
    assert 5 - 3 == 2

@pytest.mark.skip(sys.platform != "linux" , reason = "this test requires Linux")
def test_linux_
    