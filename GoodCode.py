class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second

    def multiply(self):
        return self.first * self.second

    def divide(self):
        if self.second == 0:
            return "Cannot divide by zero"
        return self.first / self.second

    def calculate(self, operation):
        if operation == "add":
            return self.add()
        elif operation == "subtract":
            return self.subtract()
        elif operation == "multiply":
            return self.multiply()
        elif operation == "divide":
           return self.divide()
        else:
            return "Invalid operation"

def get_input():
    operation = input("What operation would you like to do? (add/subtract/multiply/divide): ")
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    return operation, first, second

def main():
    operation, first, second = get_input()
    calculator = Calculator(first, second)
    result = calculator.calculate(operation)
    print(f"Result: {result}")

main()