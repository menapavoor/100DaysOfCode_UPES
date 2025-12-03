from enum import Enum

# Define enum for traffic lights
class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

# Example: set the current signal
signal = TrafficLight.GREEN

# Decide action based on signal
if signal == TrafficLight.RED:
    print("Stop")
elif signal == TrafficLight.YELLOW:
    print("Wait")
elif signal == TrafficLight.GREEN:
    print("Go")