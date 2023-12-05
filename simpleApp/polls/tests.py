from django.test import TestCase
from polls.utils import mySort

class MySortTestCase(TestCase):
    def test_mySort_empty_list(self):
        self.assertEqual(mySort(''), [])

    def test_mySort_sorted_list(self):
        self.assertEqual(mySort('1 2 3 4 5'), [1, 2, 3, 4, 5])

    def test_mySort_reverse_sorted_list(self):
        self.assertEqual(mySort('5 4 3 2 1'), [1, 2, 3, 4, 5])

    def test_mySort_unsorted_list(self):
        self.assertEqual(mySort('3 1 4 2 5'), [1, 2, 3, 4, 5])

    def test_mySort_duplicate_elements(self):
        self.assertEqual(mySort('3 1 4 2 5 3 4'), [1, 2, 3, 3, 4, 4, 5])