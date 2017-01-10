import pytest

from mergesort import merge_sort


# tests for 'mergesort'


def test_happy_flow():
    c = merge_sort([1,2,3], [2,3,4,9], 3, 4)
    assert c==[1,2,2,3,3,4,9]

def test_happy_flow2():
    c = merge_sort([1,2,3], [4,9], 3, 2)
    assert c==[1,2,3,4,9]

def test_one_no_elements():
    c = merge_sort([1,2,3], [], 3, 0)
    assert c==[1,2,3]

# FIXME: good thing above - you checked a corner case - one of the lists is empty
# ALWAYS check all corner cases - the other list is empty, both are empty

