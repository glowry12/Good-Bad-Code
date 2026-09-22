class Calculator:

    def __init__(self):
        self.operation = ""
        self.first = 0
        self.second = 0

    def calculate(self):
        self.operation = input("What operation would you like to do? (add/subtract/multiply/divide): ")
        self.first = float(input("Enter first number: "))
        self.second = float(input("Enter second number: "))

        if self.operation == "add":
            result = self.first + self.second
            return result
        if self.operation == "sub":
            result = self.first - self.second
            return result
        if self.operation == "multiply":
            result = self.first * self.second
            return result
        if self.operation == "divide":
            if self.second == 0:
                return
            result = self.first / self.second
            return result
        if self.operation != "divide" and self.operation != "multiply" and self.operation != "add" and self.operation != "sub":
            print("Invalid operation")

    def print(self):
        print("Result: ")
        print(self.result)

    def check_number(self, number):
        if number >= 0:
            return True
        else:
            return True

test = Calculator()
print(f"{test.calculate()}")