from enum import Enum

# Define enum for menu choices
class Menu(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3

# Example input: ADD 10 20
choice = Menu.ADD
a, b = 10, 20

# Perform operation using if/elif (Python doesn't have switch until 3.10)
if choice == Menu.ADD:
    print(a + b)
elif choice == Menu.SUBTRACT:
    print(a - b)
elif choice == Menu.MULTIPLY:
    print(a * b)