# importing the module
import pytest

#defining a basic function
def add_numbers(a, b):
    return a - b

def test_basic():

    assert add_numbers(3,4) == 7

if  __name__ == "__main__":
    test_basic()
