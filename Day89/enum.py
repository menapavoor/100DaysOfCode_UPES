from enum import Enum

# Define enum
class Status(Enum):
    SUCCESS = 0
    FAILURE = 1
    TIMEOUT = 2

# Print values
print(f"SUCCESS = {Status.SUCCESS.value}")
print(f"FAILURE = {Status.FAILURE.value}")
print(f"TIMEOUT = {Status.TIMEOUT.value}")