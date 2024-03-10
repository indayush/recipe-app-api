"""
Sample Tests
"""

# SimpleTestCase is for tests that dont need DB actions
from django.test import SimpleTestCase

# APIClient is for tests related to API calls
# from rest_framework.test import APIClient

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc module"""

    # It is necessary to have ""test_"" prefix to all the names of the test
    # cases
    def test_add_numbers(self):
        """Test adding"""

        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substraction"""

        res = calc.substract(15, 5)
        self.assertEqual(res, 10)
