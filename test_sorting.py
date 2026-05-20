import pytest
from sorting import merge_sort, quick_sort

def test_standard_array():
    data = [34, -2, 0, 99, 15]
    assert merge_sort(data) == sorted(data)
    assert quick_sort(data) == sorted(data)

def test_empty_array():
    assert merge_sort([]) == []
    assert quick_sort([]) == []

def test_single_element():
    assert merge_sort([42]) == [42]
    assert quick_sort([42]) == [42]

def test_already_sorted():
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    assert quick_sort([3, 2, 1]) == [1, 2, 3]

def test_identical_elements():
    assert merge_sort([7, 7]) == [7, 7]
    assert quick_sort([7, 7]) == [7, 7]
  
