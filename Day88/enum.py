from enum import Enum

# Define enum
class Colors(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2

# Loop through enum members
for color in Colors:
    print(f"{color.name} = {color.value}")