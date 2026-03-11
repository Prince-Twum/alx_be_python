class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Performs addition. 
        Static methods don't need access to class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Performs multiplication.
        Class methods receive the class (cls) as the first argument.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b