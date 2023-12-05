
import pytest
import polls
from polls.utils import mySort
def test_mySort_empty_list():
    assert mySort('') == []

def test_mySort_sorted_list():
    assert mySort('1 2 3 4 5') == [1, 2, 3, 4, 5]

def test_mySort_reverse_sorted_list():
    assert mySort('5 4 3 2 1') == [1, 2, 3, 4, 5]

def test_mySort_unsorted_list():
    assert mySort('3 1 4 2 5') == [1, 2, 3, 4, 5]

def test_mySort_duplicate_elements():
    assert mySort('3 1 4 2 5 3 4') == [1, 2, 3, 3, 4, 4, 5]

