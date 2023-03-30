"""
Unit tests for the calcs script
"""

import calcs


class TestCalculator:
    def test_addition(self):
        assert 4 == calcs.my_add_function(2, 2)

    def test_multiplication(self):
        assert 10 == calcs.myMultiplyFunction(2, 5)
