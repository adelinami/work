import pytest

from mergesort import merge_sort


# tests for 'mergesort'


def test_happy_flow():
    c = merge_sort([1,2,3], [2,3,4,9])
    assert c==[1,2,2,3,3,4,9]
    
def test_first_list_empty():
    c = merge_sort([], [1,2,3])
    assert c==[1,2,3]

def test_second_list_empty():
    c = merge_sort([1,2,3], [])
    assert c==[1,2,3]

def test_both_lists_empty():
    c = merge_sort([], [])
    assert c==[]
