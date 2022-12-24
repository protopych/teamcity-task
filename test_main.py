import pytest
from main import random_int_array, qsort, bubble_sort, merge_sort


# attempt 2
def test_buble_sort():
    arr = random_int_array()
    arr1 = arr[:]
    bubble_sort(arr1)
    assert arr1 == sorted(arr)


def test_qsort():
    arr = random_int_array()
    arr1 = arr[:]
    qsort(arr1)
    assert arr1 == sorted(arr)


def test_merge_sort():
    arr = random_int_array()
    arr1 = arr[:]
    merge_sort(arr1)
    assert arr1 == sorted(arr)
