class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def power(self, num1, num2):
        return num1 ** num2

    def calculation(self):
        total = float(input("Enter first number: "))

        while True:
            symbol = input("Enter operator (+, -, *, /, ** or = to finish): ")
            
            if symbol == "=":
                break

            num = float(input("Enter next number: "))

            if symbol == "+":
                total = self.add(total, num)
            elif symbol == "-":
                total = self.subtract(total, num)
            elif symbol == "*":
                total = self.multiply(total, num)
            elif symbol == "/":
                total = self.divide(total, num)
            elif symbol == "**":
                total = self.power(total, num)
            else:
                print("Invalid operator. Try again.")

        print("Final Total =", total)


calc = Calculator()
calc.calculation()
