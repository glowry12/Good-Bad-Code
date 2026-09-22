class Calculator:

    def __init__(self, operation, first, second):
        self.operation = operation
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
            return 0
        return self.first / self.second

    def calculate(self):
        if self.operation == "add":
            return self.add()
        elif self.operation == "subtract":
            return self.subtract()
        elif self.operation == "multiply":
            return self.multiply()
        elif self.operation == "divide":
           return self.divide()
        else:
            print("Invalid operation")

operation = input("What operation would you like to do? (add/subtract/multiply/divide): ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

test = Calculator(operation, first, second)
print(f"{test.calculate()}")