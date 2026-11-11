from src.funcs import target_and_distance
from src.calc import RaceTime

print("Enter a distance: 5k, 10k, half, full")
dist = input(" > ")  # Python 3

print("\nEnter a time:")
time = RaceTime.from_str(input(" > "))  # Python 3

print(f"\nDistance: {dist}")
print("Target Time:", time)

tpk, true_time = target_and_distance(time, dist)

print(f"Time per k: {tpk}")
print("Actual Time:", true_time)