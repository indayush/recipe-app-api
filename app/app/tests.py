"""
Sample Tests
"""


from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc module"""

    def test_add_numbers(self):
        """Test adding"""

        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substraction"""

        res = calc.substract(15, 5)
        self.assertEqual(res, 10)
