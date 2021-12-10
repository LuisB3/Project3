"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """Calculation multiplication class"""
    def get_result(self):
        """Get multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
