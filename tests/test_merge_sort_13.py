
import pytest

from mergesort.mergesort_for_13_lists import merge_sort


# tests for 'mergesort_for_13_lists'

def test_allempty():
    new_list=[]
    tuple = [], [], [], [], [], [], [], [], [], [], [], [], []
    for position in range( 13):
        new_list=merge_sort(new_list,tuple[position])
        assert new_list==[]
