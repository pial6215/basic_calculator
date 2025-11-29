# calculator.py
"""
A simple menu-driven calculator program.

Includes:
- Standalone arithmetic functions (add, subtract, multiply, divide)
- A safe input validation function
- A Calculator class that handles operations and user interaction
"""

# -------------------------
# 1) Basic arithmetic functions
# -------------------------

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """
    Perform safe division.
    Returns:
        (True, result) on success
        (False, error_message) on failure (e.g., division by zero)
    """
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, "Error: Division by zero"


# -------------------------
# 2) Input validation
# -------------------------

def get_number(prompt="Enter a number: "):
    """
    Repeatedly ask the user for a numeric input until a valid number is entered.
    Accepts integers and floats.

    Returns the value as int or float.
    """
    while True:
        value = input(prompt).strip()

        try:
            if value == "":
                raise ValueError("Empty input")

            # Detect float input
            if "." in value or "e" in value or "E" in value:
                return float(value)
            else:
                return int(value)

        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 7, 2.5).")


# -------------------------
# 3) Calculator class
# -------------------------

class Calculator:
    """A simple calculator supporting add, subtract, multiply, and divide."""

    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)

    def multiply(self, a, b):
        return multiply(a, b)

    def divide(self, a, b):
        return divide(a, b)

    def menu(self):
        """Display the calculator menu."""
        print("\n===== Simple Calculator =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def run(self):
        """
        Main loop for running the calculator.
        Shows menu → gets choice → takes numbers → prints result.
        Continues until user chooses Exit.
        """
        while True:
            self.menu()
            choice = input("Choose an option (1-5): ").strip()

            if choice not in {"1", "2", "3", "4", "5"}:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue

            if choice == "5":
                print("Exiting calculator. Goodbye!")
                break

            # Get two valid numbers
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

            # Perform the chosen operation
            if choice == "1":
                result = self.add(a, b)
                print(f"{a} + {b} = {result}")

            elif choice == "2":
                result = self.subtract(a, b)
                print(f"{a} - {b} = {result}")

            elif choice == "3":
                result = self.multiply(a, b)
                print(f"{a} * {b} = {result}")

            elif choice == "4":
                success, value = self.divide(a, b)
                if success:
                    print(f"{a} / {b} = {value}")
                else:
                    print(f"{a} / {b} -> {value}")  # Show error message


# -------------------------
# 4) Program entry point
# -------------------------

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
