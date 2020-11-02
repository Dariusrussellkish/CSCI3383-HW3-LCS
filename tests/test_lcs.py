import pylcs
import string
import random
from lcs.lcs import lcs
import pytest


def test_lcs():
    letters = string.ascii_letters
    for _ in range(1000):
        s1 = ''.join(random.choice(letters) for i in range(random.randint(1, 100)))
        s2 = ''.join(random.choice(letters) for i in range(random.randint(1, 100)))

        assert lcs(s1, s2) == pylcs.lcs(s1, s2)
    print("All test cases matched the reference implementation")
