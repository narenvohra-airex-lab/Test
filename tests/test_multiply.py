import sys
sys.path.append('../')

from src.multiply import *

def test_multiply():
    assert(multiply_numbers(3,4) == 12)

if __name__ == "__main__":
    test_multiply()
