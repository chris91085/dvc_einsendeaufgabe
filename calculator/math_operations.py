# calculator/math_operations.py

class Calculator:
    @staticmethod
    def add(a, b):
        """Addiert zwei Zahlen."""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtrahiert zwei Zahlen."""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multipliziert zwei Zahlen."""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Dividiert zwei Zahlen."""
        if b == 0:
            raise ValueError("Division durch Null ist nicht erlaubt")
        return a / b