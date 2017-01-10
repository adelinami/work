import pytest

from mergesort import merge_sort


# tests for 'mergesort'


def test_happy_flow():
    c = merge_sort([1,2,3], [2,3,4,9])
    assert c==[1,2,2,3,3,4,9]

def test_happy_flow2():
    c = merge_sort([1,2,3], [4,9])
    assert c==[1,2,3,4,9]
    
def test_corner_case_a():
    c = merge_sort([], [1,2,3])
    assert c==[1,2,3]

def test_corner_case_b():
    c = merge_sort([1,2,3], [])
    assert c==[1,2,3]

def test_corner_case_both():
    c = merge_sort([], [])
    assert c==[]
