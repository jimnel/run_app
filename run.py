from funcs import target_and_distance
from calc import Time

print("Enter a distance: 5k, 10k, half, full")
dist = input("> ")  # Python 3
print("Enter a time:")
time = input("> ")  # Python 3

target_and_distance(Time.from_str(time), dist)