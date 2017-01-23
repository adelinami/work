import pytest

from mergesort import merge_sort

def test_no_lists():
    lo = merge_sort([])
    assert lo == []

def test_happy_flow():
    c = merge_sort([[1,2,3], [2,3,4,9]])
    assert c == [1,2,2,3,3,4,9]
    

def test_lists_empty():
    c = merge_sort([[], [], []])
    assert c == []

