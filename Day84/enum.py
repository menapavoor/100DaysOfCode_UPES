from enum import Enum

# Define enum
class Status(Enum):
    SUCCESS = 1
    FAILURE = 2
    TIMEOUT = 3

# Example: set status to FAILURE
s = Status.FAILURE

# Print message based on status
if s == Status.SUCCESS:
    print("Operation successful")
elif s == Status.FAILURE:
    print("Operation failed")
elif s == Status.TIMEOUT:
    print("Operation timed out")