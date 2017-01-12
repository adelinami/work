
import pytest

from mergesort import merge_sort_13


# tests for 'mergesort_for_13_lists'

def test_allempty():
    new_list=[]
    tuple = [], [], [], [], [], [], [], [], [], [], [], [], []
    for position in range( 13):
        new_list=merge_sort_13(new_list,tuple[position])
        assert new_list==[]
